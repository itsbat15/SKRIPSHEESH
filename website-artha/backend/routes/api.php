<?php

use App\Http\Controllers\AuthController;
use App\Http\Controllers\OperationsController;
use Illuminate\Support\Facades\Route;

Route::prefix('artha')->group(function () {
    Route::post('login', [AuthController::class, 'login'])->middleware('throttle:artha-login');
    Route::middleware(['auth:sanctum', 'artha.role'])->group(function () {
        Route::post('logout', [AuthController::class, 'logout']);
        Route::get('workspace', [OperationsController::class, 'workspace']);
        Route::get('payments/{payment}/proof', [OperationsController::class, 'proof'])->whereNumber('payment');
        Route::get('payments/{payment}/receipt', [OperationsController::class, 'receipt'])->whereNumber('payment');
        Route::get('reconciliations/{close}/document', [OperationsController::class, 'closeDocument'])->whereNumber('close');

        Route::middleware('artha.role:branch_admin')->group(function () {
            Route::post('enrollments', [OperationsController::class, 'register']);
            Route::post('bills/{bill}/payments', [OperationsController::class, 'pay'])->whereNumber('bill');
            Route::post('study-groups', [OperationsController::class, 'saveGroup']);
            Route::patch('study-groups/{id}', [OperationsController::class, 'saveGroup'])->whereNumber('id');
            Route::patch('students/{id}', [OperationsController::class, 'saveStudent'])->whereNumber('id');
            Route::post('reconciliations', [OperationsController::class, 'close']);
        });

        Route::middleware('artha.role:super_admin')->group(function () {
            Route::post('branches', [OperationsController::class, 'saveBranch']);
            Route::patch('branches/{id}', [OperationsController::class, 'saveBranch'])->whereNumber('id');
            Route::post('staff', [OperationsController::class, 'saveUser']);
            Route::patch('staff/{id}', [OperationsController::class, 'saveUser'])->whereNumber('id');
            Route::post('course-packages', [OperationsController::class, 'savePackage']);
            Route::patch('course-packages/{id}', [OperationsController::class, 'savePackage'])->whereNumber('id');
            Route::patch('payments/{payment}/review', [OperationsController::class, 'reviewPayment'])->whereNumber('payment');
            Route::patch('reconciliations/{close}/approval', [OperationsController::class, 'approveClose'])->whereNumber('close');
            Route::get('reports/revenue', [OperationsController::class, 'report']);
        });
    });
});
