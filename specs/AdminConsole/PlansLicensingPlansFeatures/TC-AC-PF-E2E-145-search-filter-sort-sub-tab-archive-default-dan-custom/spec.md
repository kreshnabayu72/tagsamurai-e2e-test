---
id: TC-AC-PF-E2E-145-search-filter-sort-sub-tab-archive-default-dan-custom
title: Search, Filter, dan Sort Sub-tab Archive Default dan Custom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-357
  - TC-AC-PF-358
  - TC-AC-PF-359
  - TC-AC-PF-360
  - TC-AC-PF-362
  - TC-AC-PF-363
  - TC-AC-PF-364
  - TC-AC-PF-724
coverage:
  web: automated
---

# Search, Filter, dan Sort Sub-tab Archive Default dan Custom

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21; default aktif `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`) dan Dataset Plan R (Pre-setup #30). Default Archive berisi `Growth Plus (old)` (FAMS, Paid, 01 Aug 26 08:00), `Plan Arsip Lama` (01 Jun 26 08:00), `Plan Arsip Tengah` (15 Jul 26 08:00), `Plan Arsip Baru` (20 Aug 26 08:00); seluruhnya FAMS Paid. Dataset Plan C (Pre-setup #23): Custom Archive `Arsip Custom Satu` (v1, Clients 0, 02 Mar 26 10:00) dan `Arsip Custom Dua` (v1, historical Clients 1, 11 May 26 10:00); Custom Active `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### Default Archive

1. Klik sub-tab Archive.

#### TC-AC-PF-357 Search

2. Ketik Search `lama`, tekan Enter.
3. Verifikasi sub-tab Archive menampilkan `Plan Arsip Lama` saja.
4. Klik sub-tab Active.
5. Verifikasi sub-tab Active tidak tersaring dan menampilkan seluruh default plan aktif.
6. Klik sub-tab Archive.
7. Klik `✕` pada Search, tekan Enter.

#### TC-AC-PF-358 Filter Pricing Type dan Product

8. Buka Filter Panel dan buka dropdown Product.
9. Verifikasi opsi dropdown Product hanya `FAMS`.
10. Buka dropdown Pricing Type.
11. Verifikasi opsi dropdown Pricing Type hanya `Paid`.
12. Pilih Pricing Type `Paid` dan Product `FAMS`, klik `[Apply]`.
13. Verifikasi tabel menampilkan keempat plan archived (seluruhnya FAMS Paid).
14. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

#### TC-AC-PF-359 Filter Last Modified

15. Buka Filter Panel, pilih rentang `01 Jul 26` sampai `31 Aug 26`, klik `[Apply]`.
16. Verifikasi tabel menampilkan `Plan Arsip Baru` (20 Aug 26), `Growth Plus (old)` (01 Aug 26), dan `Plan Arsip Tengah` (15 Jul 26) berurutan Last Modified terbaru dahulu.
17. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

#### TC-AC-PF-360 Sort Last Modified

18. Klik header `Last Modified` satu kali.
19. Verifikasi `Plan Arsip Lama` (01 Jun 26) berada paling atas.
20. Klik header `Last Modified` kali kedua.
21. Verifikasi `Plan Arsip Baru` berada paling atas.
22. Klik header `Last Modified` kali ketiga.
23. Verifikasi tabel kembali ke default Newest First.

#### TC-AC-PF-724 Spasi di tengah query

24. Ketik Search `Growth Plus`, tekan Enter.
25. Verifikasi tabel menampilkan `Growth Plus (old)` saja.
26. Ganti isi kotak search dengan `Plus Growth`, tekan Enter.
27. Verifikasi empty state "No results found" tampil (query tidak dipecah menjadi kata terpisah).
28. Klik `✕` pada Search, tekan Enter.

### Custom Archive

29. Klik tab Custom, lalu sub-tab Archive.

#### TC-AC-PF-362 Search

30. Ketik Search `dua`, tekan Enter.
31. Verifikasi tabel menampilkan `Arsip Custom Dua` saja.
32. Klik `✕` pada Search, tekan Enter.

#### TC-AC-PF-363 Filter Clients dan Last Modified

33. Buka Filter Panel, isi Min Clients `1`, klik `[Apply]`.
34. Verifikasi tabel hanya menampilkan plan archived yang memiliki client (`Arsip Custom Dua`, Clients historical).
35. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.
36. Buka Filter Panel, pilih rentang `01 May 26` sampai `31 May 26`, klik `[Apply]`.
37. Verifikasi tabel menampilkan `Arsip Custom Dua`.
38. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

#### TC-AC-PF-364 Sort Last Modified dan state sub-tab

39. Klik header `Last Modified` satu kali.
40. Verifikasi `Arsip Custom Satu` berada paling atas (Oldest First).
41. Klik sub-tab Active.
42. Verifikasi sub-tab Active tetap pada sort default Plan Name A-Z.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1, 6, dan 29 berpindah tab atau sub-tab; langkah 7, 28, dan 32 mengosongkan Search (`✕` lalu Enter, bagian 8b butir 9); langkah 14, 17, 35, dan 38 mengosongkan Filter.
- Anchor absence (bagian 8b butir 2): "No results found" pada langkah 27 didahului langkah 25 (baris `Growth Plus (old)` tampil di surface yang sama).
- Alasan di atas sekitar 35 langkah (42): seluruh blok adalah kontrol tabel pada sub-tab Archive dengan dataset arsip yang sama (Default Archive memakai Dataset Plan A dan R, Custom Archive memakai Dataset Plan C), tiap blok berdiri sendiri dan tidak membangun state bagi blok berikutnya. Estimasi langkah semula lebih rendah karena S-01 memecah tiap butir Expected per klausa.
- Temuan untuk QA: (1) TC-AC-PF-358 Expected hanya menyebut "opsi dropdown hanya nilai yang ada di data sub-tab Archive" tanpa daftar nilai dan tanpa langkah membuka dropdown; spec menurunkan nilainya dari data (Product `FAMS`, Pricing Type `Paid`) dan menambah langkah membuka dropdown. (2) TC-AC-PF-363 butir a ("hanya plan archived yang memiliki client") tidak menyebut nama; spec menurunkannya dari Dataset Plan C (`Arsip Custom Dua`, historical Clients 1). (3) Dataset Plan A mendefinisikan custom archived `Enterprise Reseller` pada tenant yang sama dengan Dataset Plan C (`Arsip Custom Satu`, `Arsip Custom Dua`); TC-AC-PF-362 sampai 364 mengasumsikan Custom Archive hanya berisi dua plan Dataset Plan C. (4) Dataset Plan A dan Dataset Plan C mendefinisikan `Growth Tier` v20 dengan Last Modified berbeda (28 Jun 26 16:00 versus 22 Jun 26 08:00).
