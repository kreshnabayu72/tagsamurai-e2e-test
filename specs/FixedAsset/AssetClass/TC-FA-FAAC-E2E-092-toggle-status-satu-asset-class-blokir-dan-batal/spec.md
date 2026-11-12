---
id: TC-FA-FAAC-E2E-092-toggle-status-satu-asset-class-blokir-dan-batal
title: "Toggle Status Satu Asset Class: Diblokir D-04, Batal, Cek Ulang Server, dan Activate Idempotent"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-72
  - TC-FA-FAAC-295
  - TC-FA-FAAC-298
  - TC-FA-FAAC-299
  - TC-FA-FAAC-300
  - TC-FA-FAAC-301
  - TC-FA-FAAC-304
coverage:
  web: automated
---

# Toggle Status Satu Asset Class: Diblokir D-04, Batal, Cek Ulang Server, dan Activate Idempotent

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): sembilan Asset Class contoh Pre-setup (`HEAVY-EQ`, `VEHICLES`, `IT-EQ`, `MACHINERY`, `BLDG`, `STORAGE`, `OFFICE-NEW`, `LAND` Active dan `OFFICE-OLD` Inactive; hanya `HEAVY-EQ` yang dipakai, sisanya precondition TC, tidak diasersi), dengan `HEAVY-EQ` "Heavy Equipment" memiliki 12 Asset Name; `B-NAMES` "Names Fixture" dengan 2 Asset Name tanpa aset aktif; `B-ONE` dengan 1 Asset Name; `B-RACE3` Active tanpa Asset Name; `B-IN8` Inactive; `B-FREE10` Active tanpa Asset Name; `B-IN10` Inactive. Satu Asset Name tanpa Asset Class tersedia untuk di-assign ke `B-RACE3`.
- `HEAVY-EQ` adalah baris Pre-setup bersama yang hanya dibaca: aksi pada baris itu selalu diblokir guard (TC-72) sehingga data dan Last Updated tidak berubah (pengecualian S-06).
- Pelaku kedua: sesi API aktor (kemampuan suite, lihat suite.md): meng-assign Asset Name ke `B-RACE3` dan mengaktifkan `B-IN10` lewat fixture BE, bukan sesi UI kedua.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: assignment Asset Name pada `B-RACE3` dan status `B-IN10` kembali Inactive.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode, nama, dan jumlah Asset Name itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-72: Total Control tetap terkena guard bisnis saat Deactivate Asset Class yang punya Asset Name

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik toggle kolom Active pada baris `HEAVY-EQ` (12 Asset Name)
3. Verifikasi Dialog Blok dengan title `Cannot Deactivate Asset Class` berisi bullet `HEAVY-EQ – Heavy Equipment` dan teks `This asset class has 12 asset names. Move them to another asset class first.` dengan tombol `[OK]`
4. Klik `[OK]`
5. Verifikasi toggle Active pada baris `HEAVY-EQ` tetap On

### TC-FA-FAAC-299: Deactivate Asset Class dengan beberapa Asset Name menampilkan D-04

6. Ganti isi kotak search dengan `B-NAMES`, tekan Enter
7. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
8. Klik toggle kolom Active pada baris `B-NAMES` (On)
9. Verifikasi Dialog Blok `Cannot Deactivate Asset Class` berisi `• B-NAMES – Names Fixture` dan `This asset class has 2 asset names. Move them to another asset class first.` dengan tombol `OK`
10. Klik `OK`
11. Verifikasi toggle Active pada baris `B-NAMES` tetap On setelah dialog ditutup
12. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-300: Teks D-04 untuk satu Asset Name

13. Ganti isi kotak search dengan `B-ONE`, tekan Enter
14. Klik toggle kolom Active pada baris `B-ONE` (On)
15. Verifikasi teks dialog `This asset class has 1 asset name. Move it to another asset class first.`
16. Klik `OK`

### TC-FA-FAAC-301: Asset Class menjadi dipakai Asset Name setelah dialog Deactivate dibuka

17. Ganti isi kotak search dengan `B-RACE3`, tekan Enter
18. Klik toggle kolom Active pada baris `B-RACE3` (On)
19. Lewat sesi API aktor, assign satu Asset Name ke `B-RACE3` hingga assignment tersimpan
20. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
21. Klik `Deactivate` pada dialog
22. Verifikasi tidak ada toast yang tampil
23. Verifikasi Dialog Blok D-04 tampil (cek ulang menolak)
24. Klik `OK`
25. Verifikasi toggle Active pada baris `B-RACE3` tetap On
26. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-295: Cancel pada dialog Activate mempertahankan toggle Off

27. Ganti isi kotak search dengan `B-IN8`, tekan Enter
28. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
29. Klik toggle kolom Active pada baris `B-IN8` (Off)
30. Klik `Cancel`
31. Verifikasi tidak ada toast yang tampil
32. Verifikasi dialog menutup
33. Verifikasi toggle pada baris `B-IN8` tetap Off
34. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-298: Cancel pada dialog Deactivate mempertahankan toggle On

35. Ganti isi kotak search dengan `B-FREE10`, tekan Enter
36. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
37. Klik toggle kolom Active pada baris `B-FREE10` (On)
38. Klik `Cancel`
39. Verifikasi tidak ada toast yang tampil
40. Verifikasi dialog menutup
41. Verifikasi toggle pada baris `B-FREE10` tetap On
42. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-304: Activate atas Asset Class yang sudah Active oleh user lain bersifat idempotent

43. Ganti isi kotak search dengan `B-IN10`, tekan Enter
44. Klik toggle kolom Active pada baris `B-IN10` (Off)
45. Lewat sesi API aktor, aktifkan `B-IN10` hingga status Active tersimpan
46. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
47. Klik `Activate` pada dialog
48. Verifikasi tidak ada perubahan data: `B-IN10` tetap Active (toggle On)
49. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)
50. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: kasus diblokir guard (TC-72, TC-299, TC-300, TC-301) lebih dulu, lalu kedua kasus batal (TC-295, TC-298), dan TC-304 yang mengubah status oleh pelaku kedua di akhir.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 6, 13, 17, 27, 35, dan 43 (Search untuk menemukan baris target, R-16), langkah 7, 20, 28, 36, dan 46 (baseline Changelog, S-12), langkah 4, 10, 16, dan 24 (menutup dialog), dan langkah 50 (mengosongkan Search). Langkah 19 dan 45 adalah pemicu pelaku kedua lewat sesi API (bukan kelas c; tidak memakai P-2).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dan asersi bergantung pada kode dan jumlah Asset Name; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. S-05 dan P-1: Expected "tanpa log" pada TC-299, TC-301, TC-295, TC-298, dan TC-304 diasersi di spec ini (langkah 12, 26, 34, 42, dan 49) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class.
5. Pembagian TC: TC-72 membuka dialog blokir pada baris Pre-setup bersama dan ada di spec ini karena topik aksinya Toggle Active, bukan di spec Role Matrix.
6. Temuan untuk QA: TC-304 tidak menyebut keadaan toast setelah Activate idempotent, sehingga spec hanya mengasersi Expected "tidak ada perubahan data". Klausa "tidak ada log baru" TC-304 diasersi lewat selisih Changelog (langkah 49; butir 4).
7. Alasan melebihi sekitar 35 langkah (50 langkah): spec berisi tujuh blok TC yang masing-masing berdiri sendiri pada baris Asset Class berbeda dan satu topik aksi (Toggle Active satu Asset Class); kegagalan satu blok tidak membuat blok lain kehilangan makna dan tidak ada blok yang dipakai ulang oleh blok lain.
