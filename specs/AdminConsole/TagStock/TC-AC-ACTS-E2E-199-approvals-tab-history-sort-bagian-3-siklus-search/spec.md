---
id: TC-AC-ACTS-E2E-199-approvals-tab-history-sort-bagian-3-siklus-search
title: "Approvals Tab History: Sort 3-State Per Kelas Kolom (Bagian 3); Siklus Search Toolbar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-620
  - TC-AC-ACTS-621
coverage:
  web: automated
---

# Approvals Tab History: Sort 3-State Per Kelas Kolom (Bagian 3); Siklus Search Toolbar

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, dicatat lewat kemampuan baca fixture BE pada langkah 3 sebelum aksi (bagian 8b butir 10), bukan diturunkan dari seeding atau dibaca dari satu halaman.
- Search hanya menyaring saat Enter. Keyword siklus: `approved`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Kemampuan teknis: Pembacaan lewat fixture BE atas jumlah total baris Tab History sebagai baseline `N` (selain teks footer pagination), disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`
2. Verifikasi tabel memuat sedikitnya satu baris data

3. Catat jumlah total baris Tab History sebagai `N` (kemampuan baca fixture BE)

### TC-AC-ACTS-620: Sort 3-state kelas tanggal

4. Klik header kolom `Requested At` sekali
5. Verifikasi kolom `Requested At` Ascending (↑) (Oldest First)
6. Klik header kolom `Requested At` kedua kali
7. Verifikasi kolom `Requested At` Descending (↓) dengan urutan terbalik
8. Klik header kolom `Requested At` ketiga kali
9. Verifikasi indikator sort kolom `Requested At` hilang (netral) dan urutan kembali Resolved At Newest First
10. Klik header kolom `Resolved At` sekali
11. Verifikasi kolom `Resolved At` Ascending (↑) (Oldest First)
12. Klik header kolom `Resolved At` kedua kali
13. Verifikasi kolom `Resolved At` Descending (↓) dengan urutan terbalik
14. Klik header kolom `Resolved At` ketiga kali
15. Verifikasi indikator sort kolom `Resolved At` hilang (netral) dan urutan kembali Resolved At Newest First

### TC-AC-ACTS-621: Siklus Search toolbar

16. Hover icon Search
17. Verifikasi tooltip `Search`
18. Klik icon Search
19. Verifikasi input Search terbuka dengan fokus otomatis
20. Verifikasi placeholder input Search `Search by identifier or requester...`
21. Ketik `approved` tanpa menekan Enter
22. Verifikasi tabel belum tersaring (baris yang tidak memuat `approved` masih tampil)
23. Verifikasi icon (✕) muncul di dalam input
24. Tekan Enter
25. Verifikasi tabel memuat sedikitnya satu baris
26. Verifikasi seluruh baris yang tampil cocok dengan keyword `approved`
27. Klik icon (✕) pada input
28. Verifikasi input Search kosong
29. Verifikasi kursor tetap fokus di input Search
30. Verifikasi tabel masih menampilkan hasil search terakhir
31. Tekan Enter pada input kosong
32. Verifikasi tabel kembali menampilkan semua data (jumlah entri pada footer sama dengan `N` yang dicatat pada langkah 3)
33. Ketik Search `approved`, tekan Enter
34. Klik icon panah (←)
35. Verifikasi kotak pencarian tertutup
36. Verifikasi keyword Search dikosongkan
37. Verifikasi tabel langsung kembali menampilkan semua data (jumlah entri pada footer sama dengan `N` yang dicatat pada langkah 3)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembanding "sedikitnya satu baris" pada langkah 2 mendahului asersi urutan dan hasil Search. Asersi "semua data" memakai `N` yang dicatat pada langkah 3 lewat kemampuan baca fixture BE sebelum aksi (bagian 8b butir 10, S-12); langkah 3 hanya mencatat baseline tanpa `Verifikasi`.
- Alasan melewati sekitar 35 langkah bila dihitung dengan ekspansi: dua blok (sort kelas tanggal dan siklus Search) memakai satu dataset Tab History yang sama dan satu kelas harness (kontrol tabel), tanpa state tulis; kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah sort mengulang pola 6 langkah per kolom (bagian 8b butir 7).
