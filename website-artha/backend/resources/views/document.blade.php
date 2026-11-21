<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{{ $title }}</title>
    <style>
        body { font: 11pt "DejaVu Sans", sans-serif; color: #111118; margin: 26px; }
        header { background: #2727e6; color: white; padding: 20px; }
        h1 { font-size: 19pt; margin: 5px 0 0; }
        table { width: 100%; border-collapse: collapse; margin: 18px 0; }
        th, td { padding: 8px; border-bottom: 1px solid #cbd5e1; text-align: left; vertical-align: top; overflow-wrap: break-word; }
        th { width: 36%; }
    </style>
</head>
<body>
    <header><strong>BIMBEL ARTHA</strong><h1>{{ $title }}</h1></header>
    <p>{{ $subheading }}</p>
    <table>
        @foreach ($lines as $label => $value)
            <tr><th>{{ $label }}</th><td>{{ $value }}</td></tr>
        @endforeach
    </table>
</body>
</html>
