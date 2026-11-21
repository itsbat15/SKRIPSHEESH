<?php

use Illuminate\Database\QueryException;
use Illuminate\Foundation\Application;
use Illuminate\Foundation\Configuration\Exceptions;
use Illuminate\Foundation\Configuration\Middleware;
use Illuminate\Http\Request;

return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(api: __DIR__.'/../routes/api.php', health: '/up')
    ->withMiddleware(function (Middleware $middleware): void {
        $middleware->redirectGuestsTo(fn () => null);
        $middleware->alias(['artha.role' => App\Http\Middleware\RequireArthaRole::class]);
    })
    ->withExceptions(function (Exceptions $exceptions): void {
        $exceptions->shouldRenderJsonWhen(fn (Request $request, Throwable $e) => $request->is('api/*') || $request->expectsJson());
        $exceptions->render(function (QueryException $e, Request $request) {
            if ($request->is('api/*') && ($e->errorInfo[1] ?? null) === 1062) {
                return response()->json(['message' => 'Data sudah terdaftar. Periksa nama, tanggal lahir, atau email.'], 409);
            }
        });
    })->create();
