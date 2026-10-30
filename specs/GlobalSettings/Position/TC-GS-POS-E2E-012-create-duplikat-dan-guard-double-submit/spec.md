---
id: TC-GS-POS-E2E-012-create-duplikat-dan-guard-double-submit
title: "Create Position: Duplikat Case-Insensitive saat Mengetik, Spasi Tepi, Error Hilang saat Unik, Saving State, dan Klik Ganda Submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-47
  - TC-GS-POS-48
  - TC-GS-POS-49
  - TC-GS-POS-65
  - TC-GS-POS-66
coverage:
  web: automated
---

# Create Position: Duplikat Case-Insensitive saat Mengetik, Spasi Tepi, Error Hilang saat Unik, Saving State, dan Klik Ganda Submit

## Prerequisites

- Mode: FE+BE (backend nyata). Kasus saving state (TC-GS-POS-65) memakai intercept parsial di atas backend nyata.
- Layar awal Global Settings > User > Position dibuka hook `beforeEach`; langkah 1 langsung membuka popup Create.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (nama bersuffix per run; fixture baru `Fixture.position.createDuplicate012`):
  - Seed lewat API di hook `before`: Position `IT Manager {runId}-012` (pengganti record `IT Manager` pada Precondition c TC-GS-POS-47, 48, dan 49; Pre-setup 10 tidak dipakai).
  - Dibuat lewat UI oleh spec ini: `Compliance Officer {runId}-012` (TC-GS-POS-65) dan `Tax Specialist {runId}-012` (TC-GS-POS-66).
  - Nilai yang hanya diketik dan tidak disimpan: `it manager {runId}-012` (seluruh huruf kecil), `  IT Manager {runId}-012  ` (spasi depan dan belakang), `IT Manager {runId}-012` yang diubah menjadi `IT Manager {runId}-012 Assistant`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-012` yang masih ada (seed dan hasil Create); lepas intercept bila masih terpasang.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons Create Position 3 detik lalu melepasnya (TC-GS-POS-65; lama penahanan tidak ditetapkan TC); klik ganda cepat pada `[Submit]` (TC-GS-POS-66); pembacaan state disabled dan spinner; pembacaan jumlah toast yang tampil; menunggu hasil validasi duplikat yang muncul ±500 ms setelah berhenti mengetik.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite); intercept dilepas pada langkah 30.

## Test Steps

### TC-GS-POS-47: Nama duplikat case-insensitive terdeteksi saat mengetik

1. Klik `[+ Position]`
2. Ketik `it manager {runId}-012` (seluruh huruf kecil) pada Position Name tanpa memindahkan fokus, lalu tunggu ±500 ms
3. Verifikasi error inline "Position Name already exists" tampil ±500 ms setelah berhenti mengetik
4. Verifikasi error tampil tanpa menunggu blur (fokus masih di Position Name)
5. Verifikasi popup tetap terbuka

### TC-GS-POS-48: Nama duplikat dengan spasi depan/belakang tetap terdeteksi

6. Kosongkan Position Name (pilih seluruh teks lalu hapus)
7. Ketik `  IT Manager {runId}-012  ` (2 spasi depan, 2 spasi belakang), lalu tunggu ±500 ms
8. Verifikasi error inline "Position Name already exists" tampil (nama dibandingkan setelah trim)
9. Klik `[Submit]`
10. Verifikasi Submit ditolak (tidak ada toast sukses)
11. Verifikasi popup tetap terbuka

### TC-GS-POS-49: Error duplikat hilang setelah nama diubah menjadi unik

12. Kosongkan Position Name (pilih seluruh teks lalu hapus)
13. Ketik `IT Manager {runId}-012` pada Position Name, lalu tunggu error duplikat
14. Verifikasi error inline "Position Name already exists" tampil
15. Tambahkan ` Assistant` di akhir sehingga nama menjadi `IT Manager {runId}-012 Assistant`, lalu tunggu ±500 ms
16. Verifikasi error "Position Name already exists" hilang
17. Verifikasi border danger kembali normal

### TC-GS-POS-65: Saving state saat Submit diproses

18. Kosongkan Position Name (pilih seluruh teks lalu hapus)
19. Pasang intercept yang menahan respons Create Position selama 3 detik
20. Ketik `Compliance Officer {runId}-012` pada Position Name
21. Klik `[Submit]`
22. Verifikasi `[Submit]` menampilkan spinner
23. Verifikasi `[Submit]` disabled
24. Verifikasi input Position Name disabled
25. Verifikasi checkbox `Stay on this form after submitting` disabled
26. Verifikasi `[Clear Field]` disabled
27. Verifikasi `[✕]` disabled
28. Verifikasi setelah respons diterima, toast sukses "Success, position has been created."
29. Verifikasi popup tertutup
30. Lepas intercept penahan respons

### TC-GS-POS-66: Klik ganda Submit hanya membuat 1 record

31. Tunggu toast dari langkah 28 hilang otomatis
32. Klik `[+ Position]`
33. Ketik `Tax Specialist {runId}-012` pada Position Name
34. Klik `[Submit]` 2 kali dengan cepat
35. Verifikasi hanya 1 toast sukses "Success, position has been created." yang tampil
36. Ketik Search `Tax Specialist {runId}-012`, tekan Enter
37. Verifikasi tabel menampilkan hanya 1 baris `Tax Specialist {runId}-012`
38. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan (47, 48, 49, 65, 66). Kasus yang diblokir (TC-GS-POS-47, 48, 49) berada dalam satu pembukaan form dengan field dikosongkan di antara kasus; kasus yang berhasil (TC-GS-POS-65 dan 66) menutup form lewat Submit sukses (Stay tidak dicentang). Dua kali `[+ Position]` dibuka (langkah 1 dan 32) dan dua kejadian menutup form (langkah 29 dan setelah langkah 34).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 12, dan 18 (mengosongkan Position Name), langkah 19 dan 30 (memasang dan melepas intercept untuk TC-GS-POS-65), langkah 31 (menunggu toast sebelumnya hilang agar hitungan toast TC-GS-POS-66 tidak terpengaruh), langkah 36 (Search agar baris target tampil), dan langkah 38 (menutup input Search dan mereset tabel).
- Langkah 14 adalah `Verifikasi` tambahan di luar Expected TC-GS-POS-49: error duplikat harus tampil lebih dulu supaya Expected "error hilang" bermakna (Step 2 TC menyebut "tunggu error duplikat").
- Langkah 10 mengamati "Submit ditolak" (Expected b TC-GS-POS-48) lewat tidak adanya toast sukses; popup tetap terbuka diasersi terpisah pada langkah 11.
- Nilai `IT Manager`, `it manager`, `  IT Manager  `, dan `IT Manager Assistant` dari TC sumber diberi suffix `{runId}-012` karena record yang dideteksi duplikat adalah seed milik spec ini, bukan Pre-setup 10.
- TC-GS-POS-66 mengasersi satu baris di tabel lewat Search bersuffix karena tabel berisi data lain di environment.
- Spec berjumlah 38 langkah, sedikit di atas smell sekitar 35 langkah. Seluruhnya satu kelas (Create: duplikat dan guard Submit), satu akun; tiap blok memakai nama sendiri dan tetap bermakna bila blok lain gagal.
- Temuan untuk QA:
  - Post Condition "Tidak ada record baru" (TC-GS-POS-48), "Record `Compliance Officer` tersimpan" (TC-GS-POS-65), dan "1 record dan 1 entri Changelog Create" (TC-GS-POS-66) tidak punya langkah observasi di TC sehingga tidak diasersi, kecuali jumlah baris di tabel yang tercakup Expected b TC-GS-POS-66.
  - TC-GS-POS-65 Precondition c menyebut "Network respons create diperlambat via DevTools" tanpa lama penahanan; spec memakai 3 detik lewat `Spectra.intercept()`.
  - TC-GS-POS-47 menyebut "±500ms" tanpa batas toleransi; asersi menunggu error muncul dengan timeout yang disetel tim FE.
