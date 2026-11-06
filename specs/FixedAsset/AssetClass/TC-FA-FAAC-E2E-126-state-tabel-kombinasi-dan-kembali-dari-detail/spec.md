---
id: TC-FA-FAAC-E2E-126-state-tabel-kombinasi-dan-kembali-dari-detail
title: "State Tabel Asset Class: Kombinasi Search, Filter, Sort, dan Ukuran Halaman, serta Dipertahankan Saat Kembali dari Detail"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-384
  - TC-FA-FAAC-413
  - TC-FA-FAAC-414
coverage:
  web: automated
---

# State Tabel Asset Class: Kombinasi Search, Filter, Sort, dan Ukuran Halaman, serta Dipertahankan Saat Kembali dari Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Heavy Equipment), VEHICLES, IT-EQ (IT Equipment), MACHINERY, BLDG, STORAGE (Storage Equipment), OFFICE-NEW (Office Equipment (New)), LAND (Active) dan OFFICE-OLD (Office Equipment (Legacy), Inactive). Search `equip` mencocokkan HEAVY-EQ, IT-EQ, OFFICE-NEW, OFFICE-OLD, dan STORAGE; filter Active = Active menyisakan empat di antaranya (tanpa OFFICE-OLD). Seed disediakan tim FE/BE (lihat `suite.md`).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### TC-FA-FAAC-384: Kombinasi Search, Filter, Sort, dan ukuran halaman bersamaan

1. Ketik Search `equip`, tekan Enter
2. Klik icon Filter untuk membuka Filter Panel
3. Pilih Active = Active, klik `[Apply]`
4. Klik header Class Name dua kali (Z-A)
5. Ubah ukuran halaman ke 25
6. Verifikasi keempat kontrol (Search, Filter, Sort, ukuran halaman) berlaku bersamaan tanpa saling menimpa
7. Verifikasi urutan relatif antar baris contoh STORAGE, OFFICE-NEW, IT-EQ, HEAVY-EQ pada halaman dengan ukuran 25 (baris seed lain yang cocok `equip` dapat menyela)

### TC-FA-FAAC-413: State tabel dipertahankan saat kembali dari Detail lewat tombol Back

8. Klik Class Code HEAVY-EQ
9. Klik tombol Back browser
10. Verifikasi kembali ke tab Asset Class
11. Verifikasi Search tetap berisi `equip`
12. Verifikasi sort Class Name Z-A tetap aktif
13. Verifikasi filter Active = Active tetap aktif
14. Verifikasi ukuran halaman tetap 25
15. Verifikasi urutan relatif antar baris contoh: STORAGE, OFFICE-NEW, IT-EQ, HEAVY-EQ (baris seed lain yang cocok dapat menyela)

### TC-FA-FAAC-414: State tabel dipertahankan saat kembali dari Detail lewat breadcrumb

16. Klik Class Code HEAVY-EQ
17. Klik breadcrumb `Asset Class`
18. Verifikasi kembali ke tab Asset Class
19. Verifikasi Search tetap berisi `equip`
20. Verifikasi sort Class Name Z-A tetap aktif
21. Verifikasi filter Active = Active tetap aktif
22. Verifikasi ukuran halaman tetap 25
23. Verifikasi urutan relatif antar baris contoh: STORAGE, OFFICE-NEW, IT-EQ, HEAVY-EQ (baris seed lain yang cocok dapat menyela)

### Pemulihan

24. Klik Clear all
25. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
26. Klik header Class Name sekali lagi (sort kembali netral, Class Code A-Z)
27. Ubah ukuran halaman kembali ke 10

## Notes

- Langkah 1 sampai 5 TC-FA-FAAC-413 dan 414 identik dengan langkah TC-FA-FAAC-384 dan menghasilkan state yang sama (Search `equip`, filter Active = Active, sort Class Name Z-A, ukuran halaman 25); state itu dipakai ulang dari langkah 1 sampai 5 (S-10) dan dipertahankan setelah kembali dari Detail pada langkah 8 sampai 15, lalu 16 sampai 23. Aksi yang meninggalkan tabel (membuka Detail) diletakkan sesudah TC-FA-FAAC-384.
- Langkah penghubung (S-03): langkah 24 sampai 27 (melepas filter, menutup Search, mengembalikan sort dan ukuran halaman, S-09). Ukuran halaman 25 pada langkah 5 adalah bagian TC.
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan urutan relatif antar baris contoh, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.
