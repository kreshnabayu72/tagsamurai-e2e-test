---
id: TC-FA-CAID-E2E-015-create-pertama-company-kosong
title: "Create Konfigurasi Pertama pada Company Kosong: Save, Separator, Initial Company, dan Toggle"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-44
  - TC-FA-CAID-45
  - TC-FA-CAID-46
  - TC-FA-CAID-47
coverage:
  web: automated
---

# Create Konfigurasi Pertama pada Company Kosong: Save, Separator, Initial Company, dan Toggle

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Kosong (Pre-setup No 12); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE. Password dari `Spectra.env.FA_KOSONG_TC_PASSWORD` (nama usulan di `suite.md`, perlu konfirmasi tim FE).
- Data Pre-setup No 12: Company Kosong tanpa konfigurasi tersimpan dan tanpa aset. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): reset Company Kosong ke kondisi tanpa konfigurasi tersimpan dan tanpa aset lewat sesi API aktor (klien HTTP dan token sesi API; token tidak dihitung sebagai sesi web). Reset dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC.
- State: spec ini membuat konfigurasi pada Company Kosong. Pemulihan: hook `after` mereset Company Kosong dan mengembalikan sesi ke akun default suite (Total Control Company Alpha, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Spec ini tidak memakai data Company Alpha; baseline B1 Company Alpha tetap dipulihkan hook suite.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-44: Save pertama tanpa mengubah nilai membuat record konfigurasi

1. Klik `[Save]` tanpa mengubah kontrol apa pun
2. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
3. Verifikasi toast netral `No changes to save.` tidak tampil
4. Verifikasi tombol `[Save]` kembali disabled karena form pristine
5. Muat ulang halaman
6. Verifikasi Master Switch berada pada posisi ON
7. Verifikasi Separator menampilkan `/ (Slash)`
8. Verifikasi urutan dan status segmen default tanpa perubahan
9. Reset Company Kosong ke kondisi tanpa konfigurasi tersimpan dan tanpa aset lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman

### TC-FA-CAID-45: Save pertama dengan Separator diubah

10. Pilih Separator `- (Dash)`
11. Klik `[Save]`
12. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
13. Muat ulang halaman
14. Verifikasi Separator menampilkan `- (Dash)`
15. Verifikasi Live Preview menampilkan `JKT-LAP-T490-0926-1`
16. Reset Company Kosong ke kondisi tanpa konfigurasi tersimpan dan tanpa aset lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman

### TC-FA-CAID-46: Save pertama dengan Initial Company dicentang dan diisi

17. Centang checkbox `Initial Company`
18. Ketik `ABC` pada input Initial Company
19. Klik `[Save]`
20. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
21. Muat ulang halaman
22. Verifikasi checkbox `Initial Company` tercentang
23. Verifikasi input Initial Company berisi `ABC`
24. Verifikasi Live Preview menampilkan `ABC/JKT/LAP/T490/0926/1`
25. Reset Company Kosong ke kondisi tanpa konfigurasi tersimpan dan tanpa aset lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman

### TC-FA-CAID-47: Toggle pertama ke OFF membuat record dengan formula default

26. Geser Master Switch ke OFF
27. Klik `[Disable]` pada dialog `Disable Custom Asset ID`
28. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
29. Muat ulang halaman
30. Verifikasi Master Switch berada pada posisi OFF
31. Verifikasi Separator menampilkan `/ (Slash)`
32. Verifikasi urutan dan status segmen default tersimpan
33. Verifikasi kontrol form di-dim dan disabled
34. Verifikasi Live Preview menampilkan `1`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): langkah 9, 16, dan 25 (reset Company Kosong antar TC, karena TC berikutnya mensyaratkan konfigurasi belum pernah disimpan). Langkah pembuka "Buka tab Custom Asset ID" pada TC-FA-CAID-44 sampai TC-FA-CAID-47 dipenuhi hook `beforeEach` suite.
- Pembagian TC lintas spec: TC-FA-CAID-262 (registrasi aset pada Company Kosong tanpa konfigurasi) ada di spec 030.
- Asersi `Verifikasi` toast netral tidak tampil (langkah 3) memakai toast sukses langkah 2 sebagai anchor positif pada surface yang sama.
- Langkah 5, 13, 21, dan 29 memuat ulang halaman setelah Save sukses, sehingga form pristine dan tidak memunculkan konfirmasi `beforeunload`.
- Temuan untuk QA:
  - Email akun Total Control Company Kosong (Pre-setup No 12) tidak tertulis di Pre-setup TC; nama env var password adalah usulan.
  - TC-FA-CAID-47 tidak menyebut asersi dialog `Disable Custom Asset ID`; spec hanya mengklik `[Disable]` sesuai Langkah Uji.
