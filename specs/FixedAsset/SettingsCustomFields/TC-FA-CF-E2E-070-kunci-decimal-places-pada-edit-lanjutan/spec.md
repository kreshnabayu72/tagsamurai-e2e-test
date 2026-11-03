---
id: TC-FA-CF-E2E-070-kunci-decimal-places-pada-edit-lanjutan
title: "Kunci Decimal Places pada Edit: Pembukaan Kunci dan Penolakan Server"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-245
  - TC-FA-CF-246
  - TC-FA-CF-247
coverage:
  web: automated
---

# Kunci Decimal Places pada Edit: Pembukaan Kunci dan Penolakan Server

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor UI: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Akun pelaku kedua (sesi lain, Pre-setup #28): Total Control sesi 2 Company Nilai (pengguna Rina Putri, Pre-setup #10). Email akun ini tidak tertulis di Pre-setup TC; disediakan tim FE. Dipakai lewat sesi API (login API dengan `Spectra.env.FA_TC2_NILAI_PASSWORD`, token tidak dihitung sebagai sesi web) hanya untuk memicu perubahan state (mengosongkan atau mengisi nilai aset), sesuai `suite.md`.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Percent Used` (Percentage 1 Decimal Place, bernilai pada aset A1), `Rated Power` (Numeric 1 Decimal Place, bernilai `12.5` pada aset A1), dan `Empty Metric` (Numeric 2 Decimal Places General, tanpa nilai). Nilai yang diisi sesi API pada `Empty Metric`: `1` pada aset A1. Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan nilai aset dan field baseline yang diubah spec (`Rated Power` dan `Empty Metric` beserta nilai A1) serta membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Kemampuan teknis: hover pada radio; sesi API untuk mengosongkan dan mengisi nilai custom field aset.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-246: Decimal Places field Percentage juga terkunci bila aset menyimpan nilai

2. Klik row action `⋯` > `Edit` pada baris `Percent Used`
3. Arahkan kursor ke radio Decimal Places
4. Verifikasi radio Decimal Places disabled dengan tooltip `Decimal places can't be changed because assets already have values for this field.`
5. Klik icon close `[✕]`

### TC-FA-CF-245: Kunci Decimal Places hilang sendiri setelah tidak ada aset yang menyimpan nilai

6. Klik row action `⋯` > `Edit` pada baris `Rated Power`
7. Klik icon close `[✕]`
8. Sesi API (Rina Putri) mengosongkan nilai `Rated Power` pada seluruh aset hingga perubahan tersimpan
9. Klik row action `⋯` > `Edit` pada baris `Rated Power`
10. Verifikasi radio Decimal Places enabled
11. Verifikasi radio Decimal Places tanpa penanda terkunci
12. Klik icon close `[✕]`

### TC-FA-CF-247: Decimal Places terkunci setelah form dibuka ditolak server dengan pesan inline pada kontrol

13. Klik row action `⋯` > `Edit` pada baris `Empty Metric`
14. Pilih Decimal Places `1 (.0)`
15. Sesi API (Rina Putri) mengisi nilai `1` pada `Empty Metric` untuk aset A1 hingga perubahan tersimpan
16. Klik `[Save]`
17. Verifikasi pesan inline `Decimal places can't be changed because assets already have values for this field.` tampil pada kontrol Decimal Places
18. Verifikasi modal tetap terbuka
19. Verifikasi kontrol Decimal Places dimuat ulang terkunci
20. Verifikasi input lain dipertahankan
21. Klik icon close `[✕]`
22. Verifikasi kolom Value Setting baris `Empty Metric` menampilkan `2 Decimal Places` (tidak ada data berubah)

## Notes

- Urutan TC di spec: 246, 245, 247. Kasus yang hanya membaca (246) berjalan lebih dulu; kasus 245 dan 247 mengubah state lewat sesi API dan berada di akhir.
- Pelaku kedua hanya memicu perubahan state lewat sesi API (bukan konteks kedua kelas c); hasilnya diasersi di sesi UI pertama. Langkah 8 dan 15 ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 5, 7, 12, dan 21 (menutup modal; langkah 21 dibahas di Temuan untuk QA).
- Temuan untuk QA:
  - TC-FA-CF-247 tidak menyebut nilai yang diisi dari sesi lain; spec memakai `1` pada aset A1 sebagai nilai uji.
  - TC-FA-CF-247 tidak menyatakan apakah form dirty sesudah penolakan server (kontrol Decimal Places "dimuat ulang terkunci"); spec menganggap form bersih sehingga `[✕]` menutup modal tanpa dialog `Unsaved Changes`. Bila ternyata dirty, langkah 21 perlu `Verifikasi` dialog dan `[Leave]`.
  - Expected TC-FA-CF-245 menyebut "tanpa penanda tersimpan" tanpa menjelaskan bentuk penandanya; spec mengasersi tanpa penanda terkunci (tooltip atau status disabled).
  - TC-FA-CF-247 tidak menyebut nilai Value Setting yang diharapkan sebagai bukti "tidak ada data berubah"; spec mengasersi `2 Decimal Places` (nilai baseline `Empty Metric`).
  - Email Total Control Company Nilai (sesi 1 dan sesi 2) serta env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` dan `FA_TC2_NILAI_PASSWORD` yang disediakan tim FE.
