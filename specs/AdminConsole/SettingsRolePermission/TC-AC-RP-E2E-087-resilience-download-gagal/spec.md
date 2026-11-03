---
id: TC-AC-RP-E2E-087-resilience-download-gagal
title: "Resilience Download: Gagal pada Tabel dan Changelog Menampilkan Toast Error"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-258
  - TC-AC-RP-315
coverage:
  web: automated
---

# Resilience Download: Gagal pada Tabel dan Changelog Menampilkan Toast Error

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Download dipaksa gagal lewat `Spectra.intercept()` dan data Pre-setup dari backend nyata tidak diubah).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #13 (pemegang tingkat akses), #18 (riwayat Changelog seed), dan #23 (failure injection lewat intercept respons jaringan).
- Kebutuhan intercept (kelas b; `Spectra.intercept()`): TC-AC-RP-258 memaksa respons Download tabel Tab Total Control gagal; TC-AC-RP-315 memaksa respons Download Changelog Tab System gagal. Endpoint Download tidak didefinisikan di TC; pemetaan intercept ke endpoint disediakan tim FE. Intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis bersuffix `+{runId}-<NNN>` dan tidak ada seeding. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-258: Download gagal menampilkan toast error

1. Atur intercept: respons Download tabel Tab Total Control dipaksa gagal
2. Klik ikon Download, lalu klik Download as CSV
3. Verifikasi toast "Error, failed to download Role-Permission-Total-Control."
4. Lepas intercept respons Download
5. Tutup toast error

### TC-AC-RP-315: Download Changelog gagal

6. Klik tab `System`
7. Atur intercept: respons Download Changelog dipaksa gagal
8. Klik ikon Changelog
9. Klik ikon Download, lalu klik Download as CSV
10. Verifikasi toast "Error, failed to download Changelog-Role-Permission-System."
11. Lepas intercept respons Download
12. Tutup modal Changelog

## Notes

- Mode: FE+BE (intercept). Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Kelas harness b (fault injection); satu spec untuk dua permukaan Download (tabel Tab Total Control dan Changelog Tab System) sesuai konvensi bagian 3 prinsip 13.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 1, 4, 5, 7, 11, 12.
- Intercept dilepas segera setelah Verifikasi toast (S-09); pelepasan di hook `after` hanya jaring pengaman.
- Toast error dari TC-AC-RP-258 ditutup sebelum TC-AC-RP-315 supaya asersi toast kedua tidak membaca toast pertama (R-12).
- Langkah "Klik ikon Download, lalu klik Download as ..." membuka popover Download lalu memilih format sebagai satu aksi (PRD §4.2e; pola spec 085 langkah 1 dan 3); popover tidak diasersi di spec ini karena Expected TC tidak memuatnya.
- Temuan untuk QA:
  - TC-AC-RP-258 dan 315 menyebut "failure injection pada Download" (Pre-setup #23) tanpa kode status atau jenis kegagalan; spec memaksa respons gagal tanpa menentukan kode status, pemetaan disediakan tim FE (S-13).
  - Endpoint Download tabel dan Changelog tidak disebut TC; pemetaan intercept ke endpoint disediakan tim FE (S-13).
