---
id: TC-AC-ACAL-E2E-053-absence-aksi-modul-fams-sams-siem-dan-global-settings-tidak-masuk-tab-user-action
title: "Absence: Aksi di Modul FAMS, SAMS, SIEM, dan Global Settings Tidak Masuk Tab User Action"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACAL-163
coverage:
  web: automated
---

# Absence: Aksi di Modul FAMS, SAMS, SIEM, dan Global Settings Tidak Masuk Tab User Action

## Prerequisites

- Mode: FE+BE.
- Kelas harness g (asersi absence, bagian 3 prinsip 13): semua TC di spec ini mengasersi "tidak ada baris atau entri log" untuk kondisi yang ditolak atau tidak dicatat. Tiap TC punya baseline dan data sendiri.
- Suite serial (`parallel: false`); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen halaman Activity Log untuk akun Total Control Principal (lihat suite.md).
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Spec tidak berganti akun UI dan hook `after` tidak perlu memulihkan sesi (akun default suite).
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`:
  - User `Pengguna GS {runId}-053` dengan Position `Staff {runId}-053` (Global Settings), Position `Supervisor {runId}-053` sebagai nilai tujuan, dan aset Fixed Asset `Aset Uji {runId}-053` (TC-AC-ACAL-163).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API user, Position, dan aset dinamis di atas (atau nama hasil edit `Aset Uji {runId}-053 Baru`) bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run.
- Akses (TC-AC-ACAL-163 precondition b): akun Total Control (Principal) dapat mengakses Global Settings > User (mengubah Position user) dan Fixed Asset (mengubah nama aset); akses itu disediakan tim FE/BE.
- Kemampuan teknis (disediakan tim FE/BE):
  - Daftar nama Object dari kedua aksi saja (Position user di Global Settings > User dan nama aset di Fixed Asset) sebagai `Fixture.activityLog.objekGlobalSettingsDanFixedAsset` (nilai ditetapkan QA/tim FE; TC tidak menyebut nama Object). Object non-entitas data master platform yang memang dicatat (mis. Brand, Category, Language, Role & Permission menurut ACAL-LOGIC-01k) bukan bagian daftar ini dan tidak termasuk batasan dropdown Object.
  - Baseline (S-12): jumlah total entri dibaca dari footer `Showing X–Y of Z entries` sebelum aksi pemicu dan dibandingkan sebagai selisih, bukan angka absolut.
- Jam server dan jam browser tidak diatur. Tidak ada state global yang diubah (semua data milik spec).

## Test Steps

1. Klik tab "User Action"

### TC-AC-ACAL-163: Aksi di modul FAMS, SAMS, SIEM, dan Global Settings tidak masuk Tab User Action

2. Catat jumlah total entri dari footer `Showing X–Y of Z entries` (nilai Z) sebagai baseline G0
3. Buka Global Settings > User, ketik Search `Pengguna GS {runId}-053`, tekan Enter, lalu buka form Edit pada baris itu
4. Ubah Position menjadi `Supervisor {runId}-053`
5. Klik [Save]
6. Tunggu aksi selesai: form Edit tertutup atau tombol [Save] aktif kembali
7. Buka Fixed Asset, ketik Search `Aset Uji {runId}-053`, tekan Enter, lalu buka form Edit pada baris itu
8. Ubah nama aset menjadi `Aset Uji {runId}-053 Baru`
9. Klik [Save]
10. Tunggu aksi selesai: form Edit tertutup atau tombol [Save] aktif kembali
11. Buka Admin Console > Activity Log > User Action
12. Klik icon Filter, lalu buka dropdown Object
13. Verifikasi daftar opsi Object memuat sedikitnya satu opsi
14. Verifikasi daftar opsi Object tidak memuat Object dari kedua aksi (Position user di Global Settings > User dan nama aset di Fixed Asset; `Fixture.activityLog.objekGlobalSettingsDanFixedAsset`)
15. Tutup dropdown Object dan Filter Panel
16. Verifikasi jumlah total entri pada footer sama dengan baseline G0, sehingga tidak ada baris untuk kedua aksi

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-163).
- P-5 butir (a): spec absence boleh memuat pemicu kelas lain bila hanya membentuk kondisi yang diasersi tidak tercatat. Pemicu di sini: aksi di modul lain lewat UI (TC-AC-ACAL-163).
- Langkah penghubung (tanpa awalan `Verifikasi`): pindah tab dan menu (langkah 1, 11), pencatatan baseline (langkah 2), "Tunggu aksi selesai" (langkah 6, 10; bagian 8b butir 8), memasang dan menutup Filter (langkah 12, 15), dan mencari baris target di modul sumber lewat Search (langkah 3, 7).
- Langkah 14 hanya mengasersi ketiadaan Object dari kedua aksi; opsi Object non-entitas yang dicatat (mis. Brand) boleh ada di dropdown dan tidak diasersi.
- Asersi tambahan di luar Expected TC (S-03): langkah 13 (opsi pembanding sebelum asersi absence opsi). Asersi absence jumlah memakai baseline selisih pada surface agregat (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACAL-163 tidak menyebut data uji pelengkap (Position tujuan, nama aset, dan nama Object GS/Fixed Asset); spec memakai data bersuffix milik spec dan fixture Object.
  - TC-AC-ACAL-163 Post Condition tidak ada; cleanup nama hasil edit aset dan Position ada di hook `after`.
  - Email Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (terdaftar di `.env.example` dan `spectra.config.ts`).
