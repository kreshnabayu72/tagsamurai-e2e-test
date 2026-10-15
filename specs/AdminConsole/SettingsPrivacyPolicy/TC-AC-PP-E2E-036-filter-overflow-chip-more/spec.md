---
id: TC-AC-PP-E2E-036-filter-overflow-chip-more
title: "Filter Published By: Overflow Chip Diringkas Menjadi +N more"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-201
coverage:
  web: automated
---

# Filter Published By: Overflow Chip Diringkas Menjadi +N more

## Prerequisites

- Mode: FE+BE (kelas e, volume data khusus: enam Published By berbeda).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat V, yaitu enam Published By berbeda: `Ana Putri`, `Bimo Santoso`, `Citra Dewi`, `Dedi Kurnia`, `Eka Saputra`, `Fajar Hidayat` (satu versi masing-masing). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Spec ini hanya membaca data.
- Kemampuan teknis: Fixture BE untuk membuat ulang dataset Riwayat V (Published By tersimpan sebagai snapshot nama pada tiap versi).
- State UI yang diubah spec: draft isian panel Filter (tidak pernah di-Apply); panel ditutup tanpa Apply di akhir spec.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini sendiri tidak mengubah data.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-201: Banyak opsi Published By terpilih diringkas dalam satu chip "+N more" di dalam field

1. Buka panel Filter
2. Klik field `Published By`
3. Centang `Ana Putri`, `Bimo Santoso`, `Citra Dewi`, `Dedi Kurnia`, `Eka Saputra`, dan `Fajar Hidayat`
4. Tutup dropdown
5. Verifikasi field menampilkan chip nama sebanyak yang muat pada lebar field
6. Verifikasi sisa opsi diringkas dalam satu chip `+N more`
7. Verifikasi jumlah chip nama yang tampil ditambah N sama dengan 6
8. Verifikasi field tidak melebar keluar panel
9. Verifikasi field tidak digulir horizontal
10. Klik `[Clear Field]` lalu tutup panel Filter dengan klik di luar panel (tanpa Apply)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`. Kelas harness: e (volume data khusus; satu spec per kelas).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah menutup dropdown setelah memilih enam opsi dan langkah terakhir (membersihkan draft dan menutup panel tanpa Apply).
- Temuan untuk QA:
  - TC-AC-PP-201 Expected a menyebut "chip sebanyak yang muat pada lebar field" tanpa angka tertentu; spec mengasersi relasi jumlah chip + N = 6 (Expected b) dan keberadaan chip `+N more`, bukan jumlah chip eksak. Lebar viewport tidak disebut di TC.
  - TC-AC-PP-201 Precondition menyebut "Riwayat V tersedia" tanpa menyebut Published At tiap versi; spec tidak bergantung pada tanggal.
