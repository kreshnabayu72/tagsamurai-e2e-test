---
id: TC-AC-ACC-E2E-208-hardware-list-search-filter-dan-sort
title: "Hardware List: Search per Kolom, Filter Dropdown, dan Sort Qty"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-293
  - TC-AC-ACC-781
  - TC-AC-ACC-782
  - TC-AC-ACC-784
coverage:
  web: automated
---

# Hardware List: Search per Kolom, Filter Dropdown, dan Sort Qty

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi"; Hardware List (Tabel A3 F7): HL-1 (Handheld Reader / RFID / Brand Alfa / HR-200 / SKU-HR-200 / Qty 12) dan HL-2 (Handheld Reader / RFID / Brand Beta / HB-1 / SKU `—` / Qty 3, BYO tanpa SKU). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-293: Search Hardware List kolom teks: Category, Type, Brand, Model/Type, dan SKU

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Hardware`
4. Klik ikon Search pada toolbar Hardware List, ketik `handheld` lalu tekan Enter
5. Verifikasi Category "handheld": HL-1 (Brand Alfa, HR-200) dan HL-2 (Brand Beta, HB-1) tampil
6. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `rfid` dan tekan Enter
7. Verifikasi Type "rfid": HL-1 (Brand Alfa, HR-200) dan HL-2 (Brand Beta, HB-1) tampil
8. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `alfa` dan tekan Enter
9. Verifikasi Brand "alfa": HL-1 (Brand Alfa, HR-200) tampil
10. Verifikasi Brand "alfa": HL-2 (Brand Beta, HB-1) tidak tampil
11. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `hb-1` dan tekan Enter
12. Verifikasi Model/Type "hb-1": HL-2 (Brand Beta, HB-1) tampil
13. Verifikasi Model/Type "hb-1": HL-1 (Brand Alfa, HR-200) tidak tampil
14. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `sku-hr` dan tekan Enter
15. Verifikasi SKU "sku-hr": HL-1 (Brand Alfa, HR-200) tampil
16. Verifikasi SKU "sku-hr": HL-2 (Brand Beta, HB-1) tidak tampil

### TC-AC-ACC-781: Search Hardware List kolom numerik: Qty

17. Klik ikon ✕ pada input Search lalu tekan Enter, lalu ketik `12` dan tekan Enter
18. Verifikasi Qty "12": HL-1 (Brand Alfa, HR-200) tampil
19. Verifikasi Qty "12": HL-2 (Brand Beta, HB-1) (Qty 3) tidak tampil
20. Klik ikon ✕ pada input Search lalu tekan Enter

### TC-AC-ACC-782: Filter Hardware List kolom dropdown: Category, Type, dan Brand

21. Klik Filter, pilih Category "Handheld Reader", lalu klik `[Apply]`
22. Verifikasi Category = Handheld Reader: HL-1 (Brand Alfa, HR-200) dan HL-2 (Brand Beta, HB-1) tampil
23. Klik Filter, klik `[Clear Field]`, pilih Type "RFID", lalu klik `[Apply]`
24. Verifikasi Type = RFID: HL-1 (Brand Alfa, HR-200) dan HL-2 (Brand Beta, HB-1) tampil
25. Klik Filter, klik `[Clear Field]`, pilih Brand "Brand Alfa", lalu klik `[Apply]`
26. Verifikasi Brand = Brand Alfa: HL-1 (Brand Alfa, HR-200) tampil
27. Verifikasi Brand = Brand Alfa: HL-2 (Brand Beta, HB-1) tidak tampil
28. Klik Filter, klik `[Clear Field]`, pilih Brand "Brand Beta", lalu klik `[Apply]`
29. Verifikasi Brand = Brand Beta: HL-2 (Brand Beta, HB-1) tampil
30. Verifikasi Brand = Brand Beta: HL-1 (Brand Alfa, HR-200) tidak tampil
31. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-ACC-784: Sort Hardware List kolom Qty: urutan numerik, bukan urutan teks

32. Klik header kolom Qty satu kali
33. Verifikasi urutan ascending: HL-2 (Brand Beta, HB-1) (3), HL-1 (Brand Alfa, HR-200) (12)
34. Klik header kolom Qty untuk kedua kali
35. Verifikasi urutan descending: HL-1 (Brand Alfa, HR-200) (12), HL-2 (Brand Beta, HB-1) (3)
36. Klik header kolom Qty untuk ketiga kali
37. Verifikasi indikator sort Qty nonaktif dan urutan kembali ke default Category A-Z

## Notes

- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pencarian, penyaringan, dan pengurutan satu tabel pada satu dataset, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah mengosongkan Search (✕, Enter) dan `[Clear Field]` lalu `[Apply]` adalah langkah penghubung (S-09, D-003). Kata kunci "handheld" dan "rfid" menampilkan kedua baris sehingga anchor positif untuk asersi absence berikutnya adalah baris yang tampil pada kata kunci yang sama.
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi. TC-293 dan TC-782 mengandaikan Hardware List C-01 hanya memuat HL-1 dan HL-2; Tabel A2 tidak menyatakan baris lain.
