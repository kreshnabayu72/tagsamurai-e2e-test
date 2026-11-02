---
id: TC-AC-ACTS-E2E-139-bulk-delete-screening-checkbox-select-all-dan-kolom-checkbox
title: "Bulk Delete: Screening Bulk Action Bar, Checkbox Semua Baris Tab Available, Select All dan Unselect All, serta Kolom Checkbox (Pinned, Bukan Setup Column, Tidak Ikut Download)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-838
  - TC-AC-ACTS-839
  - TC-AC-ACTS-840
  - TC-AC-ACTS-851
coverage:
  web: automated
---

# Bulk Delete: Screening Bulk Action Bar, Checkbox Semua Baris Tab Available, Select All dan Unselect All, serta Kolom Checkbox (Pinned, Bukan Setup Column, Tidak Ikut Download)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (#12). Unit uji milik spec di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Tab Available memuat 12 unit Available dan Damaged/Missing (TC-AC-ACTS-840) serta unit Available dan Damaged/Missing untuk TC-AC-ACTS-838, 839, dan 851; skenario satu unit (TC-AC-ACTS-840) memakai SKU `RFID-SEAL-DELTA-R1` (Pre-setup #16, SKU tanpa unit) yang diberi satu unit Available oleh fixture BE.
- Kemampuan teknis: Pembaca isi berkas unduhan (header kolom CSV/XLSX), pengaturan viewport sempit, dan pembersihan preferensi kolom Setup Column di browser disediakan tim FE (hook `before` dan `after` spec ini).

## Test Steps

### TC-AC-ACTS-838: Kolom Checkbox pinned kiri dan Bulk Action Bar dengan satu aksi Delete

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Amati kolom paling kiri tabel dan header kolom Checkbox
3. Verifikasi kolom Checkbox ada di paling kiri tabel
4. Centang dua baris Available
5. Verifikasi Bulk Action Bar tampil di atas tabel rata kiri dengan teks `2 TAGs selected` dan icon `×`
6. Klik tombol `Bulk Action`
7. Verifikasi daftar aksi pada `Bulk Action` hanya `Delete`
8. Tutup daftar aksi dengan Esc, lalu klik icon `×` pada Bulk Action Bar

### TC-AC-ACTS-839: Semua baris Tab Available punya checkbox

9. Verifikasi baris Available dan baris Damaged/Missing memiliki checkbox
10. Klik checkbox header
11. Verifikasi checkbox header mencentang semua baris halaman aktif
12. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-ACTS-840: Select All dan Unselect All, teks tunggal dan jamak, hitungan semua baris

13. Centang satu baris
14. Verifikasi tombol `Select All (12 records)`
15. Klik `Select All`
16. Verifikasi tombol menjadi `Unselect All`
17. Klik `Unselect All`
18. Verifikasi seluruh seleksi dibatalkan dan Bulk Action Bar tertutup
19. Kembali ke Stock List, lalu klik row action `Detail` pada SKU `RFID-SEAL-DELTA-R1` dan buka Tab Available
20. Centang satu-satunya baris
21. Verifikasi tombol `Select All (1 record)`
22. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-ACTS-851: Kolom Checkbox pinned kiri, bukan baris Setup Column, tanpa sort/search/filter, tidak ikut Download

23. Kembali ke Stock List, lalu klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` dan buka Tab Available
24. Gulir tabel secara horizontal pada viewport sempit
25. Verifikasi kolom Checkbox tetap terlihat di kiri saat tabel digulir
26. Buka Setup Column dan Column Visibility
27. Verifikasi Checkbox tidak muncul sebagai baris pada Setup Column dan Column Visibility
28. Tutup Setup Column dengan `✕`
29. Klik header kolom Checkbox
30. Verifikasi header Checkbox tidak mengurutkan tabel
31. Ketik Search `TAG`, tekan Enter, lalu buka panel Filter
32. Verifikasi Search dan panel Filter tidak memiliki field Checkbox
33. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel, lalu tutup panel Filter
34. Klik Download dan buka berkas hasil unduhan
35. Verifikasi berkas Download tidak memuat kolom Checkbox

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), pembatalan seleksi, penutupan daftar aksi dan Setup Column dan panel Filter, navigasi antar SKU dan Stock List, serta Search `TAG` (R-16) yang mengisi tabel agar panel Search dan Filter teramati.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun dikonfirmasi tim FE.
  - Prasyarat "Reader RFID terhubung" pada keempat TC tidak berpengaruh pada Expected (Bulk Delete dan kolom Checkbox tidak memakai reader); spec tidak memakai simulator untuk asersi.
  - TC-AC-ACTS-840 Data Uji "12 unit" dan skenario 1 unit memakai SKU berbeda tanpa menyebut SKU kedua; spec memakai SKU Pre-setup tanpa unit yang diberi satu unit.
  - TC-AC-ACTS-851 tidak menyebut berkas Download (CSV atau XLSX) dan cara membaca header; spec mengasersi header kolom dengan pembaca isi berkas yang disediakan tim FE (kelas f hanya untuk isi berkas).
