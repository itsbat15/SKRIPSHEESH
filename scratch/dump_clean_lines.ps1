Add-Type -AssemblyName System.Runtime.WindowsRuntime
$asTaskGeneric = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' }

function Await($WinRtTask, $ResultType) {
    $asTask = $asTaskGeneric.MakeGenericMethod($ResultType)
    $netTask = $asTask.Invoke($null, @($WinRtTask))
    $netTask.Wait(-1) | Out-Null
    $netTask.Result
}

[Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime] | Out-Null

$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()

for ($p = 1; $p -le 5; $p++) {
    $imgPath = "C:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\scratch\page_${p}_clean.png"
    $file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($imgPath)) ([Windows.Storage.StorageFile])
    $stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
    $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bitmap = Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $ocrResult = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])

    $linesOut = @()
    foreach ($line in $ocrResult.Lines) {
        $minX = [double]::MaxValue
        $minY = [double]::MaxValue
        $maxRight = [double]::MinValue
        $maxBottom = [double]::MinValue

        foreach ($w in $line.Words) {
            $rect = $w.BoundingRect
            if ($rect.X -lt $minX) { $minX = $rect.X }
            if ($rect.Y -lt $minY) { $minY = $rect.Y }
            if ($rect.Right -gt $maxRight) { $maxRight = $rect.Right }
            if ($rect.Bottom -gt $maxBottom) { $maxBottom = $rect.Bottom }
        }

        $linesOut += [PSCustomObject]@{
            Text = $line.Text
            X = [Math]::Round($minX, 1)
            Y = [Math]::Round($minY, 1)
            W = [Math]::Round($maxRight - $minX, 1)
            H = [Math]::Round($maxBottom - $minY, 1)
        }
    }
    $json = $linesOut | ConvertTo-Json -Depth 3
    [System.IO.File]::WriteAllText("C:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\scratch\p${p}_boxes.json", $json, [System.Text.Encoding]::UTF8)
    Write-Output "Page $p saved ($($linesOut.Count) lines)"
}

