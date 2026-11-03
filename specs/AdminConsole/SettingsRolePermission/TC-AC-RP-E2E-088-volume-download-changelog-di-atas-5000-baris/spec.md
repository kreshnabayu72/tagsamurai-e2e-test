---
id: TC-AC-RP-E2E-088-volume-download-changelog-di-atas-5000-baris
title: "Volume: Download Changelog di Atas 5.000 Baris Memakai Loading Screen"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-316
coverage:
  web: automated
---

# Volume: Download Changelog di Atas 5.000 Baris Memakai Loading Screen

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Distributor `Distributor Seleksi Besar` `totalControlBigRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hadi Gunawan`), password dari `Spectra.env.AC_RP_BIG_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #20, entitas `Distributor Seleksi Besar` dengan lebih dari 5.000 entri Changelog System (volume disiapkan lewat seed atau API oleh tim FE/BE; spec tidak membuat volume). Halaman dibuka sebagai Distributor, bukan Principal.
- Kemampuan teknis: membaca nama berkas yang terunduh dari folder unduhan browser (disediakan tim FE) dan membaca status job background (disediakan tim FE/BE; TC tidak menyebut cara cek job).
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis bersuffix `+{runId}-<NNN>` dan tidak ada seeding. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_BIG_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

1. Klik tab `System`
2. Klik ikon Changelog
3. Klik ikon Download, lalu klik Download as XLSX
4. Verifikasi loading screen tampil
5. Verifikasi tidak ada toast sukses yang tampil
6. Verifikasi berkas Changelog System terunduh
7. Verifikasi loading screen tidak lagi tampil setelah berkas terunduh
8. Verifikasi tidak ada job background yang dibuat
9. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Kelas harness e (volume data khusus: lebih dari 5.000 entri Changelog System).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 9.
- Asersi loading screen diletakkan segera setelah pemicu (bagian 8b butir 5) dan asersi absence toast sukses segera sesudahnya, sebelum Verifikasi berkas terunduh yang menjadi anchor positif (bagian 8b butir 11).
- Expected "Loading screen tampil sampai berkas siap lalu berkas langsung terunduh" diuraikan menjadi Verifikasi loading tampil, berkas terunduh, dan loading tidak lagi tampil (S-01).
- Langkah "Klik ikon Download, lalu klik Download as ..." membuka popover Download lalu memilih format sebagai satu aksi (PRD §4.2e; pola spec 085 langkah 1 dan 3); popover tidak diasersi di spec ini karena Expected TC tidak memuatnya.
- Temuan untuk QA:
  - TC-AC-RP-316 tidak menyebut nama berkas hasil Download Changelog Tab System format XLSX; spec hanya mengasersi berkas terunduh, bukan nama berkas.
  - TC-AC-RP-316 Expected "tanpa job background" tidak memberi cara observasi; spec memakai kemampuan baca status job yang disediakan tim FE/BE (S-11, S-13).
  - Jumlah "lebih dari 5.000 entri" tidak diasersi di UI; volume dijamin Pre-setup #20.
