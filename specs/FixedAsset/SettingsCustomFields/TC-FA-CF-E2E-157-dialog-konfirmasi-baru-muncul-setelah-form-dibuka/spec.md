---
id: TC-FA-CF-E2E-157-dialog-konfirmasi-baru-muncul-setelah-form-dibuka
title: "Dialog Konfirmasi yang Baru Muncul Setelah Form Dibuka (Data Type, Global, Scope)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-601
  - TC-FA-CF-602
  - TC-FA-CF-603
coverage:
  web: automated
---

# Dialog Konfirmasi yang Baru Muncul Setelah Form Dibuka (Data Type, Global, Scope)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor UI: Total Control Company Nilai (Company Alpha ditambah aset dengan nilai, Pre-setup #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Pelaku kedua: Total Control sesi 2 Company Nilai lewat sesi API (login API dengan `Spectra.env.FA_TC2_NILAI_PASSWORD`, token tidak dihitung sebagai sesi web; lihat `suite.md`). Email akun ini tidak tertulis di Pre-setup TC; disediakan tim FE. Password tidak ditulis di spec atau fixture. Nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup Company Nilai (Pre-setup #18): `Empty Metric` Numeric 2 Decimal Places General tanpa nilai; `Rated Power` Numeric 1 Decimal Place Scope {Generator, Pump} bernilai `12.5` pada aset `A1`; aset `A1` (Pump), `A2` (Generator). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture disediakan tim FE).
- Kemampuan teknis: sesi API aktor untuk mengisi nilai aset (kemampuan disediakan tim BE/FE); seed reset Company Nilai (disediakan tim FE/BE).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: nilai aset `Empty Metric` dan `Rated Power` diubah oleh spec; hook `before` dan `after` memulihkan Company Nilai lewat seed reset. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-601: dialog Change Data Type yang baru muncul

1. Klik row action `⋯` > `Edit` pada baris `Empty Metric`
2. Ganti Data Type menjadi `Text`
3. Sesi API (Total Control sesi 2) menambahkan nilai `Empty Metric` pada satu aset hingga nilai tersimpan
4. Klik `[Save]`
5. Verifikasi dialog `Change Data Type` tampil
6. Verifikasi modal Edit tetap terbuka
7. Klik `[Change Data Type]` pada dialog
8. Verifikasi Save diulang dengan konfirmasi eksplisit dan sukses dengan toast `Success, custom field has been updated.`
9. Pulihkan Company Nilai ke baseline lewat seed reset, lalu muat ulang Settings > Custom Fields

### TC-FA-CF-602: dialog Change to Global Value yang baru muncul

10. Klik row action `⋯` > `Edit` pada baris `Empty Metric`
11. Pilih Value Type `Global` dengan Value `3`
12. Sesi API (Total Control sesi 2) menambahkan nilai aset pada `Empty Metric` hingga nilai tersimpan
13. Klik `[Save]`
14. Verifikasi dialog `Change to Global Value` tampil
15. Verifikasi modal Edit tetap terbuka
16. Klik `[Change to Global]` pada dialog
17. Verifikasi Save diulang dan sukses (modal Edit tertutup)

### TC-FA-CF-603: dialog Change Scope yang baru muncul

18. Klik row action `⋯` > `Edit` pada baris `Rated Power`
19. Hapus chip `Generator` dari Scope
20. Sesi API (Total Control sesi 2) menambahkan nilai aset `Generator` (aset `A2`) pada `Rated Power` hingga nilai tersimpan
21. Klik `[Save]`
22. Verifikasi dialog `Change Scope` tampil
23. Verifikasi modal Edit tetap terbuka
24. Klik `[Change Scope]` pada dialog
25. Verifikasi Save diulang dan sukses (modal Edit tertutup)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua memicu perubahan state lewat sesi API (bukan konteks kedua kelas c; hasil asersi hanya di sesi UI pertama), ditulis "... hingga ... tersimpan" (R-20); `P-2` tidak dipakai (keputusan 2026-10-30).
- Langkah 9 (seed reset Company Nilai) adalah langkah penghubung (aksi tanpa `Verifikasi`) karena `Empty Metric` dipakai dua TC dan precondition kedua TC menuntut `Empty Metric` belum bernilai.
- Langkah 8, 17, dan 25 mengasersi sukses Save yang diulang: TC-FA-CF-601 menyebut toast `Success, custom field has been updated.`; TC-FA-CF-602 dan 603 hanya menyebut "Save diulang dan sukses" sehingga spec mengasersi modal Edit tertutup.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company Nilai; akun disediakan tim FE.
  - TC-FA-CF-601 sampai 603 bertanda Manual Only (dua sesi paralel) padahal sesi 2 hanya menambahkan nilai aset sebagai pemicu state; spec memakai sesi API.
  - TC-FA-CF-602 dan 603 tidak menyebut indikator "Save diulang dan sukses" (toast atau penutupan modal).
