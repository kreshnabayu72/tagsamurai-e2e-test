---
id: TC-AC-ACTS-E2E-158-detail-sku-retensi-state-per-sub-tab-hapus-baris-terakhir-dan-identifier-non-rfid
title: "Detail SKU: State Per Sub-Tab, Refresh F5, Hapus Baris Terakhir di Halaman Terakhir, dan Kolom Identifier (UID, RFID) Kosong untuk Non-RFID"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-795
  - TC-AC-ACTS-787
  - TC-AC-ACTS-801
  - TC-AC-ACTS-789
coverage:
  web: automated
---

# Detail SKU: State Per Sub-Tab, Refresh F5, Hapus Baris Terakhir di Halaman Terakhir, dan Kolom Identifier (UID, RFID) Kosong untuk Non-RFID

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (#12) dengan >= 11 unit Available ber-TAG Code memuat `TAG-4F` (hasil Search `tag-4f` dengan Filter Status Available masih > 10 baris) dan >= 11 unit In Use milik Client `PT Maju Bersama` untuk TC-AC-ACTS-787 dan 801; SKU `NFC-CARD-BETA-N2` (#13) dengan unit Available dan unit In Use untuk TC-AC-ACTS-795; TC-AC-ACTS-789 memakai 11 unit Available pada SKU RFID (10 baris per halaman) lalu SKU `RFID-SEAL-DELTA-R1` (#16) dengan satu unit Available. Unit uji milik spec di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`; Last Updated SKU Pre-setup berubah akibat Delete (efek dipulihkan fixture BE).

## Test Steps

### TC-AC-ACTS-795: Kolom `Identifier (UID, RFID)` tampil `—` untuk unit non-RFID di Tab Available dan Tab In Use

1. Klik row action `Detail` pada SKU `NFC-CARD-BETA-N2` di Stock List
2. Amati kolom `Identifier` dan `Identifier (UID, RFID)` di Tab Available
3. Verifikasi Tab Available: kolom `Identifier` berisi UID Code unit dan `Identifier (UID, RFID)` tampil `—`
4. Buka Tab In Use dan amati kedua kolom yang sama
5. Verifikasi Tab In Use: kolom `Identifier` berisi UID Code unit dan `Identifier (UID, RFID)` tampil `—`

### TC-AC-ACTS-787: State Search, Filter, Sort, dan paginasi disimpan per sub-tab di Detail SKU

6. Buka Stock List, lalu klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`
7. Di Tab Available: ketik Search `tag-4f`, tekan Enter
8. Terapkan Filter Status = Available
9. Urutkan kolom TAG Code Ascending
10. Pindah ke halaman 2
11. Pindah ke Tab In Use dan amati
12. Verifikasi Tab In Use tampil default (state Tab Available tidak terbawa)
13. Di Tab In Use: ketik Search `maju`, tekan Enter
14. Terapkan Filter Client = `PT Maju Bersama`
15. Pindah ke halaman 2
16. Kembali ke Tab Available
17. Verifikasi Tab Available memulihkan Search, Filter, Sort, halaman, dan jumlah baris miliknya sendiri
18. Pindah ke Tab In Use
19. Verifikasi Tab In Use memulihkan Search, Filter, halaman, dan jumlah baris miliknya sendiri
20. Klik menu sidebar TAG > Stock, lalu buka lagi Detail SKU `RFID-ASSET-CORE-R5`
21. Verifikasi Tab Available kembali ke default
22. Pindah ke Tab In Use
23. Verifikasi Tab In Use kembali ke default

### TC-AC-ACTS-801: State Search, Filter, Sort, dan paginasi dipertahankan saat refresh F5

24. Buka Tab Available: ketik Search `tag-4f`, tekan Enter
25. Terapkan Filter Status = Available
26. Urutkan kolom TAG Code Ascending
27. Pindah ke halaman 2
28. Tekan F5
29. Verifikasi Tab Available setelah F5: Search, Filter, Sort, halaman aktif, dan jumlah baris per halaman sama seperti sebelum refresh
30. Buka Tab In Use: ketik Search `maju`, tekan Enter
31. Terapkan Filter Client = `PT Maju Bersama`
32. Pindah ke halaman 2
33. Tekan F5
34. Verifikasi Tab In Use setelah F5: Search, Filter, halaman aktif, dan jumlah baris per halaman sama seperti sebelum refresh
35. Klik menu sidebar TAG > Stock, lalu buka lagi Detail SKU `RFID-ASSET-CORE-R5` untuk memulihkan state default

### TC-AC-ACTS-789: Hapus baris terakhir di halaman terakhir Tab Available memindahkan tabel ke halaman terakhir yang masih ada

36. Reset dataset: 11 unit Available lewat fixture BE, lalu buka Tab Available
37. Pindah ke halaman 2 (1 baris)
38. Klik (⋯) pada baris itu, klik `Delete`, lalu klik `[Delete]`
39. Verifikasi tabel pindah ke halaman 1 (halaman terakhir yang masih ada), bukan halaman kosong
40. Buka Stock List, lalu klik row action `Detail` pada SKU `RFID-SEAL-DELTA-R1` (satu unit Available) dan buka Tab Available
41. Klik (⋯) pada satu-satunya unit, klik `Delete`, lalu klik `[Delete]`
42. Verifikasi empty state `No available TAGs` dengan Description `Available TAGs ready for pairing or deployment will appear here.`

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu topik (Detail SKU, satu SKU dan satu dataset); tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah pembukaan Detail SKU dan pemulihan state diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), navigasi sidebar yang mereset state, Search `tag-4f` dan `maju` (R-16), "Reset dataset", dan pembukaan Detail SKU lain. Urutan TC: 795, 787, 801, 789; aksi menghapus data (TC-AC-ACTS-789) di akhir (prinsip 5).
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - TC-AC-ACTS-787 dan 801 mensyaratkan >= 11 unit Available ber-TAG Code `TAG-4F` dan >= 11 unit In Use milik Client `PT Maju Bersama` (cocok Search `maju`); Pre-setup dan Dinamis TC tidak mendaftarnya, sehingga dari seeding spec.
  - TC-AC-ACTS-787 Expected butir a-c menyebut state "Search, Filter, Sort, halaman, dan jumlah baris" dalam satu butir; spec mengasersi tiap tab dalam satu Verifikasi karena TC menyebut daftarnya utuh.
  - Langkah Uji TC-AC-ACTS-789 nomor 3 "untuk SKU yang hanya punya satu unit" memakai SKU lain tanpa menyebutnya; spec memakai `RFID-SEAL-DELTA-R1` (Pre-setup #16) dengan satu unit seeding.
