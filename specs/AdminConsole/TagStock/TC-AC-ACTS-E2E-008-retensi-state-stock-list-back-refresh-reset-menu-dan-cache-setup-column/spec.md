---
id: TC-AC-ACTS-E2E-008-retensi-state-stock-list-back-refresh-reset-menu-dan-cache-setup-column
title: "Retensi State Stock List: Back dari Detail SKU, Refresh F5, Reset Klik Menu Sidebar, dan Cache Setup Column Independen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-30
  - TC-AC-ACTS-31
  - TC-AC-ACTS-32
  - TC-AC-ACTS-112
  - TC-AC-ACTS-113
coverage:
  web: automated
---

# Retensi State Stock List: Back dari Detail SKU, Refresh F5, Reset Klik Menu Sidebar, dan Cache Setup Column Independen

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 dan SKU RFID #12.
- Data seed milik spec (SKU bersuffix `{runId}-008`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): 26 SKU RFID ber-Brand `Core` agar kombinasi Search `core` dan Filter TAG Type RFID menghasilkan lebih dari 25 baris sehingga halaman 2 dengan 25 baris per halaman terisi.
- Pemulihan Setup Column: TC-AC-ACTS-112 dan 113 menyimpan konfigurasi kolom; langkah penghubung mengembalikan kolom dan hook `after` menghapus preferensi kolom tabel di browser (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-30: State list dipertahankan saat Back dari Detail SKU

1. Ketik Search `core`, tekan Enter
2. Klik icon Filter, pilih `RFID` pada field `TAG Type`, klik `[Apply]`
3. Klik header `Total Registered` sekali sampai Ascending
4. Ubah Rows per page menjadi 25, lalu pindah ke halaman 2
5. Klik teks Device Name baris pertama untuk membuka Detail SKU, lalu klik breadcrumb `Stock`
6. Verifikasi Search tetap `core`
7. Verifikasi Filter TAG Type RFID tetap aktif
8. Verifikasi Sort Total Registered Ascending tetap aktif
9. Verifikasi Halaman aktif tetap halaman 2
10. Verifikasi Jumlah baris per halaman tetap 25

### TC-AC-ACTS-31: State list dipertahankan saat refresh F5

11. Tekan F5
12. Verifikasi Search tetap `core`
13. Verifikasi Filter TAG Type RFID tetap aktif
14. Verifikasi Sort Total Registered Ascending tetap aktif
15. Verifikasi Halaman aktif tetap halaman 2
16. Verifikasi Jumlah baris per halaman tetap 25

### TC-AC-ACTS-32: Klik ulang menu sidebar mereset list ke default

17. Klik menu sidebar TAG > Stock
18. Verifikasi Search kosong
19. Verifikasi Filter kosong
20. Verifikasi Sort default Last Updated Newest First
21. Verifikasi Halaman 1
22. Verifikasi 10 baris per halaman

### TC-AC-ACTS-112: Cache Setup Column independen, ubah Stock List tidak mengubah Tab Available

23. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available dan catat susunan header kolom, lalu klik breadcrumb `Stock`
24. Klik header (⋯), klik `[Setup Column]`, hilangkan centang kolom `Brand`, klik `[Save]`
25. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
26. Verifikasi Susunan kolom Tab Available sama dengan yang dicatat sebelum perubahan (tidak terpengaruh)
27. Klik breadcrumb `Stock`, klik header (⋯), klik `[Setup Column]`, centang kembali kolom `Brand`, klik `[Save]`

### TC-AC-ACTS-113: Cache Setup Column independen, ubah Tab Available tidak mengubah Stock List

28. Catat susunan header kolom Stock List
29. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available, klik header (⋯), klik `[Setup Column]`, hilangkan centang kolom `Status`, klik `[Save]`
30. Klik breadcrumb `Stock`
31. Verifikasi Susunan kolom Stock List sama dengan yang dicatat sebelum perubahan (tidak terpengaruh)
32. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available, klik header (⋯), klik `[Setup Column]`, centang kembali kolom `Status`, klik `[Save]`

## Notes

- Urutan TC mengikuti TC sumber; TC-AC-ACTS-31 melanjutkan state yang dibangun TC-AC-ACTS-30 (Dependensi TC-AC-ACTS-30); TC-AC-ACTS-32 mereset state itu dan TC-AC-ACTS-112 serta 113 dijalankan sesudahnya dengan Search dan Filter kosong sesuai precondition.
- Langkah penghubung (S-03): mengatur Search, Filter, Sort, Rows per page, dan halaman membangun state TC-AC-ACTS-30; mencatat susunan header kolom sebelum perubahan sebagai baseline TC-AC-ACTS-112 dan 113; mengembalikan kolom `Brand` dan `Status` sesudah asersi.
- Temuan untuk QA (S-15): TC-AC-ACTS-112 dan 113 menyebut "Tab Available dan tabel lain tidak terpengaruh" / "Stock List tidak terpengaruh" tanpa menyebut kolom yang dicek; spec membandingkan susunan header kolom terhadap baseline yang dicatat. TC-AC-ACTS-30 tidak menyebut data uji untuk halaman 2 dengan 25 baris; spec men-seed 26 SKU RFID ber-Brand `Core`.
