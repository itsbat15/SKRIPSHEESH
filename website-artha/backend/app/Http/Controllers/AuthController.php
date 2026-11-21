<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;

class AuthController
{
    public function login(Request $request): JsonResponse
    {
        $input = $request->validate(['email' => 'required|email:rfc|max:200', 'password' => 'required|string|max:128']);
        $user = User::where('email', strtolower($input['email']))->first();
        $dummy = '$2y$12$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi';
        $valid = Hash::check($input['password'], $user?->password ?? $dummy);
        abort_unless($valid && $user?->hasAccess(), 401, 'Email atau kata sandi salah.');
        $user->tokens()->where('expires_at', '<=', now())->delete();
        $token = $user->createToken('simba-web', ['artha'], now()->addHours(8));
        return response()->json(['token' => $token->plainTextToken, 'role' => $user->role])
            ->header('Cache-Control', 'private, no-store');
    }

    public function logout(Request $request): JsonResponse
    {
        $request->user()->currentAccessToken()->delete();
        return response()->json(['ok' => true]);
    }
}
