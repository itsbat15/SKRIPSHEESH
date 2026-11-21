<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('branches', function (Blueprint $table) {
            $table->id();
            $table->string('name', 200)->unique();
            $table->string('address', 400);
            $table->boolean('active')->default(true);
        });
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->foreignId('branch_id')->nullable()->constrained();
            $table->string('name', 200);
            $table->string('email', 200)->unique();
            $table->string('password');
            $table->enum('role', ['super_admin', 'branch_admin']);
            $table->boolean('active')->default(true);
            $table->timestamps();
        });
        DB::statement("ALTER TABLE users ADD CONSTRAINT user_role_branch CHECK ((role='super_admin' AND branch_id IS NULL) OR (role='branch_admin' AND branch_id IS NOT NULL))");
        Schema::create('personal_access_tokens', function (Blueprint $table) {
            $table->id();
            $table->morphs('tokenable');
            $table->text('name');
            $table->string('token', 64)->unique();
            $table->text('abilities')->nullable();
            $table->timestamp('last_used_at')->nullable();
            $table->timestamp('expires_at')->nullable()->index();
            $table->timestamps();
        });
        Schema::create('course_packages', function (Blueprint $table) {
            $table->id();
            $table->string('name', 200);
            $table->enum('level', ['TK', 'SD', 'SMP', 'SMA']);
            $table->unsignedBigInteger('registration_fee');
            $table->unsignedBigInteger('monthly_fee');
            $table->boolean('active')->default(true);
            $table->unique(['name', 'level']);
        });
        Schema::create('study_groups', function (Blueprint $table) {
            $table->id();
            $table->foreignId('branch_id')->constrained();
            $table->string('name', 200);
            $table->enum('level', ['TK', 'SD', 'SMP', 'SMA']);
            $table->string('schedule', 200);
            $table->unsignedSmallInteger('capacity');
            $table->boolean('active')->default(true);
            $table->unique(['branch_id', 'name']);
            $table->unique(['id', 'branch_id']);
        });
        Schema::create('students', function (Blueprint $table) {
            $table->id();
            $table->foreignId('branch_id')->constrained();
            $table->string('name', 200);
            $table->date('birth_date');
            $table->string('school', 200);
            $table->enum('level', ['TK', 'SD', 'SMP', 'SMA']);
            $table->string('guardian', 200);
            $table->string('phone', 24);
            $table->string('address', 400);
            $table->unique(['branch_id', 'name', 'birth_date']);
            $table->unique(['id', 'branch_id']);
        });
        Schema::create('enrollments', function (Blueprint $table) {
            $table->id();
            $table->foreignId('branch_id')->constrained();
            $table->unsignedBigInteger('student_id');
            $table->unsignedBigInteger('group_id');
            $table->foreignId('package_id')->constrained('course_packages');
            $table->date('registered_on');
            $table->unsignedTinyInteger('due_day');
            $table->unsignedBigInteger('monthly_fee');
            $table->enum('status', ['pending', 'active', 'inactive']);
            $table->foreign(['student_id', 'branch_id'])->references(['id', 'branch_id'])->on('students');
            $table->foreign(['group_id', 'branch_id'])->references(['id', 'branch_id'])->on('study_groups');
            $table->index(['group_id', 'status']);
            $table->unique(['id', 'branch_id']);
        });
        Schema::create('tuition_bills', function (Blueprint $table) {
            $table->id();
            $table->foreignId('branch_id')->constrained();
            $table->unsignedBigInteger('enrollment_id');
            $table->enum('kind', ['registration', 'tuition']);
            $table->char('period', 7);
            $table->date('due_on');
            $table->unsignedBigInteger('amount');
            $table->foreign(['enrollment_id', 'branch_id'])->references(['id', 'branch_id'])->on('enrollments');
            $table->unique(['enrollment_id', 'kind', 'period']);
            $table->unique(['id', 'branch_id']);
        });
        Schema::create('payments', function (Blueprint $table) {
            $table->id();
            $table->foreignId('branch_id')->constrained();
            $table->unsignedBigInteger('bill_id');
            $table->foreignId('recorded_by')->constrained('users');
            $table->enum('method', ['cash', 'transfer']);
            $table->enum('status', ['confirmed', 'pending', 'rejected']);
            $table->unsignedBigInteger('amount');
            $table->date('recorded_on');
            $table->date('recognized_on')->nullable();
            $table->string('sender', 200)->nullable();
            $table->date('transfer_on')->nullable();
            $table->foreignId('reviewed_by')->nullable()->constrained('users');
            $table->timestamp('reviewed_at')->nullable();
            $table->string('rejection_reason', 400)->nullable();
            $table->foreign(['bill_id', 'branch_id'])->references(['id', 'branch_id'])->on('tuition_bills');
            $table->index(['bill_id', 'status']);
            $table->index(['branch_id', 'recognized_on']);
        });
        Schema::create('payment_proofs', function (Blueprint $table) {
            $table->foreignId('payment_id')->primary()->constrained('payments');
            $table->string('file_type', 50);
            $table->binary('body');
        });
        DB::statement('ALTER TABLE payment_proofs MODIFY body MEDIUMBLOB NOT NULL');
        Schema::create('daily_reconciliations', function (Blueprint $table) {
            $table->id();
            $table->foreignId('branch_id')->constrained();
            $table->foreignId('closed_by')->constrained('users');
            $table->date('day');
            $table->unsignedBigInteger('cash');
            $table->unsignedBigInteger('transfer');
            $table->unsignedBigInteger('physical');
            $table->string('note', 400)->nullable();
            $table->enum('status', ['submitted', 'needs_review', 'approved']);
            $table->foreignId('reviewed_by')->nullable()->constrained('users');
            $table->timestamp('reviewed_at')->nullable();
            $table->unique(['branch_id', 'day']);
        });
    }

    public function down(): void
    {
        foreach (['daily_reconciliations', 'payment_proofs', 'payments', 'tuition_bills', 'enrollments', 'students',
            'study_groups', 'course_packages', 'personal_access_tokens', 'users', 'branches'] as $table) {
            Schema::dropIfExists($table);
        }
    }
};
