---
id: TC-FA-FAAC-E2E-189-siklus-hidup-asset-name-dan-deactivate
title: "Siklus Hidup Asset Name dan Deactivate: Diblokir saat Ada Asset Name, Diizinkan setelah Dipindah, Di-Unassign, atau Dihapus, serta Aktivasi Ulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-638
  - TC-FA-FAAC-639
  - TC-FA-FAAC-640
  - TC-FA-FAAC-641
  - TC-FA-FAAC-642
coverage:
  web: automated
---

# Siklus Hidup Asset Name dan Deactivate: Diblokir saat Ada Asset Name, Diizinkan setelah Dipindah, Di-Unassign, atau Dihapus, serta Aktivasi Ulang

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Asset Class anchor TC-638 (seed Pre-setup, hasil TC-FA-FAAC-87): `B-ANCHOR` (`Anchor Heavy Equipment`, Active, tanpa Asset Name ter-assign); fixture BE menyetel keadaan awal itu sebelum TC-638.
- Data seed Pre-setup (kode dan nama literal TC, disediakan fixture BE): Asset Name tanpa Asset Class `Hand Truck` (TC-638) dan `Whiteboard Easel` (0 aset aktif, TC-642); Asset Class `SPARE-EQ3` (`Spare Class 3`, Active) dengan satu Asset Name `Pump Rack` (0 aset aktif); `SPARE-EQ4` (`Spare Class 4`, Active) dengan satu Asset Name `Pump Rack 2` (0 aset aktif); `SPARE-EQ5` (`Spare Class 5`, Active) dengan satu Asset Name `Pump Rack 3` (0 aset aktif); `MACHINERY` (Active) dengan Asset Name `Pump Set 2`; `OFFICE-OLD` (`Office Equipment (Legacy)`, Inactive) tanpa Asset Name. Spec mengubah keanggotaan Asset Name (termasuk `Hand Truck` pada `B-ANCHOR`), status `OFFICE-OLD`, dan menghapus `Pump Rack 3`; fixture BE memulihkan seed tersebut di hook `after` (efek Last Updated dan entri Changelog tidak dapat dipulihkan).
- Kemampuan teknis: sesi API aktor (kemampuan suite, lihat suite.md) untuk menghapus Asset Name `Pump Rack 3` hingga penghapusan tersimpan, setara aksi TC-641 di Settings > Asset Master > Asset Name (modul lain di luar suite ini).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-638: Deactivate ditolak setelah Asset Name di-assign ke Asset Class

1. Ketik Search `B-ANCHOR`, tekan Enter
2. Buka Detail `B-ANCHOR`, klik tab `Asset Names`, lalu assign `Hand Truck` (klik `+ Assign Asset Names`, centang `Hand Truck`, klik `[Assign]`)
3. Tunggu aksi selesai
4. Kembali ke tabel Asset Class (klik breadcrumb `Asset Class`), lalu klik toggle Active pada baris `B-ANCHOR` (posisi On)
5. Verifikasi Dialog Blok tampil: Title `Cannot Deactivate Asset Class`, Body `• B-ANCHOR – Anchor Heavy Equipment` dan `This asset class has 1 asset name. Move it to another asset class first.`, tombol `[OK]`
6. Klik `[OK]`
7. Verifikasi toggle Active baris `B-ANCHOR` tetap On

### TC-FA-FAAC-639: Deactivate diizinkan setelah Asset Name terakhir dipindah keluar

8. Ganti isi kotak search dengan `SPARE-EQ3`, tekan Enter
9. Buka Detail `SPARE-EQ3`, klik tab `Asset Names`, lalu Move `Pump Rack` ke `MACHINERY` (klik ikon `⋯` pada baris `Pump Rack`, pilih `Move`, pilih `Destination Asset Class` = `MACHINERY`, klik `[Move]`)
10. Tunggu aksi selesai
11. Kembali ke tabel Asset Class (klik breadcrumb `Asset Class`), lalu klik toggle Active baris `SPARE-EQ3`
12. Verifikasi dialog konfirmasi tampil, bukan Dialog Blok: Title `Deactivate Asset Class`, Body `• SPARE-EQ3 – Spare Class 3` dan `Are you sure you want to deactivate it?`, tombol `[Cancel]` dan `[Deactivate]`
13. Klik `[Cancel]`
14. Verifikasi toggle Active baris `SPARE-EQ3` tetap On

### TC-FA-FAAC-640: Deactivate diizinkan setelah Asset Name terakhir di-Unassign

15. Ganti isi kotak search dengan `SPARE-EQ4`, tekan Enter
16. Buka Detail `SPARE-EQ4`, klik tab `Asset Names`, lalu Unassign `Pump Rack 2` (klik ikon `⋯` pada baris `Pump Rack 2`, pilih `Unassign`, klik `[Unassign]`)
17. Tunggu aksi selesai
18. Kembali ke tabel Asset Class (klik breadcrumb `Asset Class`), lalu klik toggle Active baris `SPARE-EQ4`
19. Verifikasi dialog konfirmasi tampil: Title `Deactivate Asset Class`, Body `• SPARE-EQ4 – Spare Class 4` dan `Are you sure you want to deactivate it?`, tombol `[Cancel]` dan `[Deactivate]`
20. Klik `[Cancel]`
21. Verifikasi toggle Active baris `SPARE-EQ4` tetap On

### TC-FA-FAAC-641: Deactivate diizinkan setelah Asset Name terakhir dihapus dari modul Asset Name

22. Lewat sesi API aktor, hapus Asset Name `Pump Rack 3` hingga penghapusan tersimpan (setara menghapus di Settings > Asset Master > Asset Name)
23. Ganti isi kotak search dengan `SPARE-EQ5`, tekan Enter
24. Klik toggle Active baris `SPARE-EQ5`
25. Verifikasi dialog konfirmasi tampil: Title `Deactivate Asset Class`, Body `• SPARE-EQ5 – Spare Class 5` dan `Are you sure you want to deactivate it?`, tombol `[Cancel]` dan `[Deactivate]`
26. Klik `[Cancel]`

### TC-FA-FAAC-642: Asset Class yang diaktifkan kembali dapat menerima Assign dan Move

27. Ganti isi kotak search dengan `OFFICE-OLD`, tekan Enter
28. Aktifkan `OFFICE-OLD` lewat toggle Active, lalu klik `[Activate]` pada dialog konfirmasi
29. Tunggu aksi selesai
30. Buka Detail `OFFICE-OLD`, klik tab `Asset Names`, lalu assign `Whiteboard Easel` (klik `+ Assign Asset Names`, centang `Whiteboard Easel`, klik `[Assign]`)
31. Verifikasi toast sukses `Success, asset name has been assigned.`
32. Verifikasi Dialog Blok D-20 tidak muncul
33. Kembali ke tabel Asset Class (klik breadcrumb `Asset Class`), lalu ganti isi kotak search dengan `MACHINERY`, tekan Enter
34. Buka Detail `MACHINERY`, klik tab `Asset Names`, klik ikon `⋯` pada baris `Pump Set 2`, pilih `Move`, lalu buka daftar `Destination Asset Class`
35. Verifikasi opsi `OFFICE-OLD – Office Equipment (Legacy)` tersedia pada daftar `Destination Asset Class`
36. Klik `[Cancel]` pada dialog Move

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Spec ini topik siklus hidup Asset Name terhadap aksi Deactivate; tiap TC memakai Asset Class dan Asset Name miliknya sendiri.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 8, 15, 23, 27, dan 33 memakai Search untuk menemukan baris target (R-16); langkah "Tunggu aksi selesai" (3, 10, 17, dan 29) sesudah assign, Move, Unassign, dan `[Activate]` yang hasilnya tidak diasersi langsung sebelum pindah surface; langkah 6, 13, 20, dan 26 menutup dialog dengan `[OK]` atau `[Cancel]`; langkah 22 adalah pelaku kedua lewat sesi API ("... hingga ... tersimpan", R-20), bukan konteks UI kedua dan tidak memakai P-2; langkah 36 menutup dialog Move dengan `[Cancel]`, yang tidak memunculkan dialog `Unsaved Changes` menurut Catatan Cakupan TC-698 dan TC-699.
3. Pengecualian kode dan nama seed literal (S-06/S-12): TC mewajibkan `B-ANCHOR`, `SPARE-EQ3`, `SPARE-EQ4`, `SPARE-EQ5`, `OFFICE-OLD`, `MACHINERY`, serta nama Asset Name literal; nilai dipakai apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nilai itu. Target aksi tulis adalah seed yang dipulihkan fixture BE di hook `after`; efek Last Updated dan entri Changelog dicatat di Prerequisites. 
4. Alasan jumlah langkah: jumlah nominal 36 langkah melampaui sekitar 35 langkah karena lima TC siklus hidup Asset Name yang tiap bloknya memakai Asset Class dan Asset Name sendiri serta empat langkah penghubung "Tunggu aksi selesai" (8b butir 8); semua TC satu topik dan tiap blok berdiri sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
5. Temuan untuk QA: TC-638 memakai anchor `B-ANCHOR – Anchor Heavy Equipment` (hasil TC-FA-FAAC-87); spec memakai seed itu dan fixture BE memulihkan keanggotaan Asset Name-nya. TC-639 sampai TC-641 tidak menyebut label tombol konfirmasi Move atau Unassign dan TC-639 tidak menyebut Effective From untuk Move Asset Name tanpa aset aktif; spec mengikuti TC. TC-641 menghapus Asset Name di modul Asset Name lewat UI; spec memakai sesi API aktor (S-04: dependensi lewat seeding API) dan tidak mengasersi UI modul itu. TC-642 mengaktifkan `OFFICE-OLD` Pre-setup (Inactive) sebagai target aksi tulis; fixture BE memulihkan statusnya.
