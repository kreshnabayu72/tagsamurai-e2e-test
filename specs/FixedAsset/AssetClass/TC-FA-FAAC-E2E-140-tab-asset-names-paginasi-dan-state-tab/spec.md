---
id: TC-FA-FAAC-E2E-140-tab-asset-names-paginasi-dan-state-tab
title: "Tab Asset Names: Paginasi, Ukuran Halaman, Search pada Halaman 2, dan State Tabel antar Tab Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-467
  - TC-FA-FAAC-468
  - TC-FA-FAAC-469
  - TC-FA-FAAC-470
  - TC-FA-FAAC-471
coverage:
  web: automated
---

# Tab Asset Names: Paginasi, Ukuran Halaman, Search pada Halaman 2, dan State Tabel antar Tab Detail

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (hanya dibaca): Asset Class Active 'Warehouse Equipment' (`WH-EQ`) memiliki 12 Asset Name ter-assign `Pallet Rack A` sampai `Pallet Rack L`.
- Kode dan nama seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `WH-EQ`, tekan Enter
2. Klik link Class Code `WH-EQ` di tabel
3. Klik tab `Asset Names`

### TC-FA-FAAC-467: Paginasi default 10 baris per halaman dengan pilihan ukuran halaman

4. Verifikasi halaman 1 memuat 10 baris dengan ukuran halaman 10
5. Klik halaman 2
6. Verifikasi halaman 2 memuat 2 baris
7. Buka pilihan jumlah data per halaman
8. Verifikasi pilihan ukuran halaman 10, 25, 50, dan 100

### TC-FA-FAAC-468: Mengubah ukuran halaman ke 25 menampilkan seluruh baris

9. Ubah ukuran halaman menjadi 25
10. Verifikasi seluruh 12 baris tampil pada satu halaman
11. Ubah ukuran halaman kembali menjadi 10

### TC-FA-FAAC-469: Search pada halaman 2 mengembalikan tabel ke halaman 1

12. Klik halaman 2
13. Ketik Search `Pallet Rack A`, tekan Enter
14. Verifikasi tabel kembali ke halaman 1
15. Verifikasi tabel menampilkan hasil pencarian `Pallet Rack A`
16. Klik `(←)` pada kotak Search

### TC-FA-FAAC-471: State tabel direset saat meninggalkan halaman Detail

17. Ketik Search `Pallet Rack`, tekan Enter
18. Klik breadcrumb `Asset Class` untuk kembali ke tabel
19. Klik link Class Code `WH-EQ` di tabel
20. Klik tab `Asset Names`
21. Verifikasi kotak Search kosong
22. Verifikasi sort default Asset Name A-Z
23. Verifikasi ukuran halaman 10
24. Verifikasi tidak ada filter aktif

### TC-FA-FAAC-470: State Search, Sort, dan ukuran halaman dipertahankan saat pindah tab Detail lalu kembali

25. Ketik Search `Pallet Rack`, tekan Enter
26. Urutkan kolom `Asset Name` Z-A (klik header dua kali)
27. Pilih ukuran halaman 25
28. Klik tab `Depreciation`
29. Klik tab `Asset Names`
30. Verifikasi Search `Pallet Rack` tetap berlaku
31. Verifikasi sort `Asset Name` Z-A tetap berlaku
32. Verifikasi ukuran halaman 25 tetap berlaku

## Notes

1. Pengecualian nama seed literal: TC mewajibkan baris seed bernama literal (`HEAVY-EQ` dan Asset Name-nya) dan asersi bergantung pada nama itu; seed dipakai apa adanya tanpa suffix `{runId}` dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Perubahan urutan TC: TC-471 ditulis sebelum TC-470 supaya spec berakhir pada TC yang meninggalkan state tabel yang diubah (Search, Sort, ukuran halaman) tanpa langkah pemulihan; state tabel itu hilang saat halaman Detail ditinggalkan dan bukan state form (S-09).
3. Detail `WH-EQ` dibuka sekali di awal dan sekali lagi pada TC-471 karena TC itu menguji pembukaan ulang Detail.
4. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 sampai 3, 11, 16, 18 sampai 20, termasuk Search untuk menemukan baris target (R-16).
