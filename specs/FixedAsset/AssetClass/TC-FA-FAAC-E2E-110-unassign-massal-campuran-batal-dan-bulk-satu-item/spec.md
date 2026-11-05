---
id: TC-FA-FAAC-E2E-110-unassign-massal-campuran-batal-dan-bulk-satu-item
title: "Unassign Massal: Dialog Campuran dengan Batal, Lanjutkan Melewati Aset Aktif, dan Bulk Satu Item"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-233
  - TC-FA-FAAC-234
  - TC-FA-FAAC-239
coverage:
  web: automated
---

# Unassign Massal: Dialog Campuran dengan Batal, Lanjutkan Melewati Aset Aktif, dan Bulk Satu Item

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Construction Equipment` (`CONSTR-EQ`) dengan Asset Name ter-assign `Bulldozer D6` (5 aset aktif), `Concrete Mixer` (0 aset aktif), dan `Tower Light` (0 aset aktif); Asset Class Active `Machinery` (`MACHINERY`) dengan Asset Name ter-assign `Ladder Steel` dan `Safety Cone Set` (masing-masing 0 aset aktif).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: `Concrete Mixer` dan `Tower Light` kembali ter-assign ke `CONSTR-EQ`.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama dan jumlah aset aktif itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `CONSTR-EQ`, tekan Enter
2. Klik link Class Code `CONSTR-EQ` di tabel
3. Klik tab `Asset Names`

### TC-FA-FAAC-234: Batal pada dialog Unassign campuran mempertahankan seleksi

4. Centang baris `Bulldozer D6` dan `Concrete Mixer`, lalu klik `Bulk Action` dan pilih `Unassign`
5. Klik `[Cancel]` pada dialog campuran
6. Verifikasi tidak ada toast yang tampil
7. Verifikasi dialog menutup dan tidak ada Asset Name yang dilepas (`Bulldozer D6` dan `Concrete Mixer` tetap tampil)
8. Verifikasi kedua baris tetap tercentang (seleksi dipertahankan)
9. Klik `Unselect All`

### TC-FA-FAAC-233: Unassign massal campuran dengan lanjutkan melewati Asset Name yang memiliki aset aktif

10. Centang baris `Bulldozer D6`, `Concrete Mixer`, dan `Tower Light`, lalu klik `Bulk Action` dan pilih `Unassign`
11. Verifikasi Dialog `Unassign Asset Names` berisi `The following will be unassigned:` dengan bullet `• Concrete Mixer`, `• Tower Light`, `The following still have active assets and will be skipped:` dengan bullet `• Bulldozer D6 — has active assets`, dan `Are you sure you want to continue?` dengan footer `[Cancel]` dan `[Continue]`
12. Klik `[Continue]`
13. Verifikasi toast sukses parsial `Success, asset name has been unassigned. Some items were skipped (still has active assets).`
14. Verifikasi `Concrete Mixer` dan `Tower Light` hilang dari tab Asset Names
15. Verifikasi `Bulldozer D6` tetap tampil
16. Klik breadcrumb `Asset Class`

### TC-FA-FAAC-239: Bulk Unassign dengan tepat satu item terpilih menampilkan dialog single

17. Ganti isi kotak search dengan `MACHINERY`, tekan Enter
18. Klik link Class Code `MACHINERY` di tabel
19. Klik tab `Asset Names`
20. Centang baris `Ladder Steel` saja, lalu klik `Bulk Action` dan pilih `Unassign`
21. Verifikasi Dialog versi single dengan Title `Unassign Asset Name`, body `• Ladder Steel` dan `It will have no asset class and its assets will not be depreciated. Are you sure you want to unassign it?` (bukan `Unassign Asset Names`)
22. Klik `[Cancel]`
23. Verifikasi dialog menutup tanpa perubahan (`Ladder Steel` tetap tampil)
24. Klik `Unselect All`
25. Klik breadcrumb `Asset Class`
26. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: TC-234 (batal, tanpa perubahan data) lebih dulu, lalu TC-233 yang melepas Asset Name, dan TC-239 pada Asset Class lain di akhir. Detail `CONSTR-EQ` dibuka sekali di langkah 2 dan 3 untuk TC-234 dan TC-233.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan 17 (Search untuk menemukan baris target, R-16), langkah 9 dan 24 (membersihkan seleksi, S-09), langkah 16 dan 25 (kembali ke tabel), dan langkah 26 (mengosongkan Search).
3. Pengecualian kode seed literal: TC mewajibkan Asset Class dan Asset Name seed bernama literal dengan jumlah aset aktif tertentu; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Rujukan S-05: tidak ada klausa "tanpa log" pada TC di spec ini yang diasersi sebagai absence.
5. Pembagian TC: Unassign single, menu baris, dan blokir massal ada di spec 090 dan 091.
6. Temuan untuk QA: Post Condition TC-233 ("hanya dua Asset Name yang menjadi tanpa Asset Class") tidak punya langkah observasi sendiri di TC; spec mengasersi hasilnya lewat Expected c (baris hilang dan baris `Bulldozer D6` tetap tampil). Precondition TC-239 menyebut `Safety Cone Set` tetapi langkah TC hanya memakai `Ladder Steel`.
