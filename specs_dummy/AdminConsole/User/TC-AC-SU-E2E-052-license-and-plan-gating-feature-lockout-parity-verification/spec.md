---
id: TC-AC-SU-E2E-052-license-and-plan-gating-feature-lockout-parity-verification
title: "Verifikasi Ketiadaan Plan Gating dan Paritas Fitur Lengkap di Seluruh Tingkat Langganan"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-202
  - TC-AC-SU-203
coverage:
  web: automated
---

# Verifikasi Ketiadaan Plan Gating dan Paritas Fitur Lengkap di Seluruh Tingkat Langganan

## Prerequisites

- Pengujian dilakukan pada beberapa organisasi tenant dengan paket langganan berbeda: Tenant Paket Starter / Basic dan Tenant Paket Enterprise

## Test Steps

### Verifikasi Paritas Fitur pada Paket Starter / Basic
1. Login sebagai Administrator pada tenant dengan paket langganan `Starter / Basic`
2. Buka menu `Admin Console > Settings > User`
3. Verifikasi seluruh fitur utama tersedia penuh:
   - Pencarian, filter multi-kriteria, sorting, dan navigasi sidebar grup
   - Halaman Detail User, Tab Role (Global Role & Group Role), Tab Responsibilities
   - Tab Changelog, System Log, dan User Log
   - Fitur ekspor CSV/XLSX dan aksi seleksi massal (Bulk Action Bar)
4. Verifikasi TIDAK ADA fitur yang terkunci dengan badge upgrade, watermark gembok, atau dialog pemblokiran lisensi
5. Pastikan modul Settings User diperlakukan sebagai fondasi tata kelola platform yang setara di seluruh paket produk

## Notes

Memastikan ketiadaan batasan lisensi komersial pada fitur tata kelola dasar pengguna.
