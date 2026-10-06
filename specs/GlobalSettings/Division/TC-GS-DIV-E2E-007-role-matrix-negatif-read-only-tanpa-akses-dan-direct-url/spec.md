---
id: TC-GS-DIV-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url
title: "Role Matrix Negatif: Read Only, Pengguna Tanpa Akses, dan Direct URL 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-08
  - TC-GS-DIV-13
  - TC-GS-DIV-14
coverage:
  web: automated
---

# Role Matrix Negatif: Read Only, Pengguna Tanpa Akses, dan Direct URL 403

## Prerequisites

- Tersedia akun dengan Role: Read Only dan akun tanpa capability Manage user and role

## Test Steps

1. Login sebagai pengguna dengan Role: Read Only
2. Buka menu Global Settings > User > tab Division
3. Verifikasi tab Division dapat diakses dalam mode baca murni: tombol '[+ Division]' tersembunyi, checkbox seleksi tersembunyi, row action (⋯) tersembunyi, sedangkan tabel, Search, Filter, Download, dan Changelog tetap tampil aktif
4. Login sebagai pengguna tanpa izin Manage user and role
5. Buka menu Global Settings > User
6. Verifikasi tab 'Division' tersembunyi total dari navigasi sub-tab
7. Akses URL langsung tab Division melalui address bar browser
8. Verifikasi sistem menolak akses dengan halaman Forbidden / pesan 403 atau me-redirect pengguna ke landing page yang diizinkan

## Notes

- Pengamanan ganda (Defense-in-depth) diatur pada division.md §9.3 dan prd-conventions.md §18.6.
