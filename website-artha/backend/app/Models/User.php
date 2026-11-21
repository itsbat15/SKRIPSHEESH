<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Support\Facades\DB;
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens;

    protected $fillable = ['name', 'email', 'password', 'role', 'branch_id', 'active'];

    protected $hidden = ['password'];

    protected function casts(): array
    {
        return ['password' => 'hashed', 'active' => 'boolean', 'branch_id' => 'integer'];
    }

    public function isCenter(): bool
    {
        return $this->role === 'super_admin';
    }

    public function hasAccess(): bool
    {
        return $this->active && ($this->isCenter() || DB::table('branches')->where('id', $this->branch_id)->where('active', 1)->exists());
    }

    public function scopeStaff(Builder $query): Builder
    {
        return $query->where('role', 'branch_admin');
    }
}
