<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class RequireArthaRole
{
    public function handle(Request $request, Closure $next, ?string $role = null): Response
    {
        $user = $request->user();
        abort_unless($user && $user->hasAccess(), 401, 'Akun atau cabang tidak aktif. Silakan masuk kembali.');
        abort_if($role && $user->role !== $role, 403, 'Anda tidak memiliki akses.');
        $response = $next($request);
        $response->headers->set('Cache-Control', 'private, no-store');
        $response->headers->set('X-Content-Type-Options', 'nosniff');
        return $response;
    }
}
