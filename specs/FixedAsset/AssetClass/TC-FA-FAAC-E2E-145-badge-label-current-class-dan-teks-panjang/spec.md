---
id: TC-FA-FAAC-E2E-145-badge-label-current-class-dan-teks-panjang
title: "Picker Assign: Badge Label dengan Chip +N more dan Badge Current Class Terpotong, serta Teks Class Name dan Asset Name Sangat Panjang"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-685
  - TC-FA-FAAC-694
  - TC-FA-FAAC-695
coverage:
  web: automated
---

# Picker Assign: Badge Label dengan Chip +N more dan Badge Current Class Terpotong, serta Teks Class Name dan Asset Name Sangat Panjang

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (hanya dibaca): Asset Name 'Label Rich Unit' (Label Heavy, Insured, Rented, Fleet) ter-assign ke Asset Class `B-LABELS`; Asset Class Active `B-TRUNC` tersedia sebagai Asset Class yang dibuka pada TC-694 dan memiliki Asset Name `Climate Probe` (seed Pre-setup, hanya dibaca; dasar `Verifikasi` langkah 24); Asset Class Active `B-LONGNM` dengan Class Name 'Heavy Duty Mining Equipment Fleet' (33 karakter) memiliki Asset Name 'Dump Truck HD785' (0 aset aktif); Asset Class Active `B-LONGTXT` dengan Class Name 'Peralatan Berat Pertambangan Batubara Kalimantan Timur Unit Produksi Gabungan Wilayah Operasi Tambang Terbuka Blok Delta' (120 karakter) memiliki Asset Name 'Excavator Hidrolik Kapasitas Besar Untuk Tambang Terbuka Blok Delta' (67 karakter; 0 aset aktif).
- Data Dinamis: Asset Class Active tanpa Asset Name ter-assign dengan Class Code literal `ANCHOR-145` dan Class Name `Anchor Class {runId}-145`, dibuat lewat API di hook `before` (setelah menghapus sisa run sebelumnya) dan dihapus di hook `after` (lihat Notes); dipakai sebagai Asset Class yang dibuka pada TC-685 dan tidak diubah.
- Kode dan nama seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-685: Kolom Label picker Assign menampilkan dua Badge dan chip +N more

1. Ketik Search `ANCHOR-145`, tekan Enter
2. Klik link Class Code `ANCHOR-145` di tabel
3. Klik tab `Asset Names`
4. Klik tombol `+ Assign Asset Names`
5. Hilangkan centang `Without asset class only`
6. Ketik Search `Label Rich Unit` pada kotak `Search asset name...`, tekan Enter
7. Verifikasi kolom Label baris `Label Rich Unit` menampilkan dua Badge `Heavy` dan `Insured`
8. Verifikasi kolom Label baris `Label Rich Unit` menampilkan satu chip `+2 more`
9. Klik chip `+2 more`
10. Verifikasi popover berisi daftar lengkap Label `Heavy`, `Insured`, `Rented`, dan `Fleet`
11. Klik `Cancel` pada dialog picker Assign

### TC-FA-FAAC-694: Badge Current Class Class Name lebih dari 25 karakter terpotong, hover menampilkan Class Code dan Class Name lengkap

12. Klik breadcrumb `Asset Class`
13. Ganti isi kotak search dengan `B-TRUNC`, tekan Enter
14. Klik link Class Code `B-TRUNC` di tabel
15. Klik tab `Asset Names`
16. Klik tombol `+ Assign Asset Names`
17. Hilangkan centang checkbox `Without asset class only`
18. Ketik Search `Dump Truck HD785` pada kotak `Search asset name...`, tekan Enter
19. Verifikasi badge Current Class baris `Dump Truck HD785` tampil `Heavy Duty M..ipment Fleet` (12 huruf pertama, `..`, 12 huruf terakhir), bukan Class Name penuh
20. Arahkan kursor ke badge Current Class baris `Dump Truck HD785`
21. Verifikasi tooltip menampilkan `B-LONGNM – Heavy Duty Mining Equipment Fleet`
22. Klik `Cancel`
23. Verifikasi dialog picker Assign tertutup
24. Verifikasi tabel Asset Names `B-TRUNC` memuat baris `Climate Probe`
25. Verifikasi tabel Asset Names `B-TRUNC` tidak memuat `Dump Truck HD785` (Asset Name tidak dipindahkan)

### TC-FA-FAAC-695: Teks datar Class Name dan Asset Name sangat panjang tampil utuh tanpa pemotongan dan tanpa tooltip

26. Klik breadcrumb `Asset Class`
27. Ganti isi kotak search dengan `B-LONGTXT`, tekan Enter
28. Verifikasi sel Class Name baris `B-LONGTXT` tampil utuh 120 karakter
29. Verifikasi sel Class Name baris `B-LONGTXT` tanpa `..` dan tanpa ellipsis
30. Verifikasi kolom Class Name melebar mengikuti isi (hug content)
31. Arahkan kursor ke teks Class Name
32. Verifikasi hover teks Class Name tidak menampilkan tooltip
33. Klik link Class Code `B-LONGTXT`
34. Klik tab `Asset Names`
35. Verifikasi Asset Name pada tab Asset Names tampil utuh 67 karakter
36. Verifikasi Asset Name tanpa `..` dan tanpa ellipsis
37. Verifikasi kolom Asset Name melebar mengikuti isi
38. Arahkan kursor ke teks Asset Name
39. Verifikasi hover teks Asset Name tidak menampilkan tooltip

## Notes

1. Pengecualian nama seed literal: TC mewajibkan baris seed bernama literal (`HEAVY-EQ` dan Asset Name-nya) dan asersi bergantung pada nama itu; seed dipakai apa adanya tanpa suffix `{runId}` dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Urutan: TC-685 memakai Asset Class milik spec (`ANCHOR-145`) yang dibuka sekali; TC-694 dan TC-695 memakai Asset Class seed yang disebut TC (`B-TRUNC`, `B-LONGTXT`).
3. Anchor absence: 'tidak menampilkan tooltip' (TC-695) didahului `Verifikasi` teks Class Name dan Asset Name tampil di surface yang sama; 'tidak memuat Dump Truck HD785' (TC-694) didahului `Verifikasi` baris `Climate Probe` tampil di tabel yang sama (bagian 8b butir 2).
4. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 6, 11 sampai 15, 18, 26, 27, termasuk Search untuk menemukan baris target (R-16).
5. Alasan melebihi sekitar 35 langkah (39 langkah): semua blok membaca tab atau modal yang sama dengan data Pre-setup yang sama, tidak mengubah data, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
6. Class Code `ANCHOR-145` ditulis literal dan `{runId}-145` dipindah ke Class Name karena Class Code dibatasi 15 karakter sehingga `ANCHOR-{runId}-145` tidak muat (S-12, nama literal; pola spec 066 sampai 069; kode berbeda antar spec); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu (cleanup tidak berasumsi setup berhasil penuh). Link Class Code dicari lewat Search kode literal itu (R-16).
