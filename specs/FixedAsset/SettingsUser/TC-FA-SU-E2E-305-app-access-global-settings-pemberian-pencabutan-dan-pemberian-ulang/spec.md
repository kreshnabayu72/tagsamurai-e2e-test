---
id: TC-FA-SU-E2E-305-app-access-global-settings-pemberian-pencabutan-dan-pemberian-ulang
title: "App Access Global Settings: Pemberian, Pencabutan, dan Pemberian Ulang"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-941
  - TC-FA-SU-942
  - TC-FA-SU-943
coverage:
  web: automated
---

# App Access Global Settings: Pemberian, Pencabutan, dan Pemberian Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan Global Settings (#38). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Pengguna Baru {runId}-305`, email `pengguna.baru+{runId}-305@qwertysystem.net`: identitas ada di Global Settings tanpa App Access FAMS (target TC-FA-SU-941); kredensial aktivasi dan login pengguna ini disediakan tim FE.
  - `Wawan Setiawan {runId}-305`, email `wawan.setiawan+{runId}-305@qwertysystem.net`: Active; Global Role, Group Role (Manage files pada IT Infrastructure), Transaction Role, dan Home Group terisi (target TC-FA-SU-942).
  - `Wawan Setiawan 2 {runId}-305`, email `wawan.setiawan+{runId}-305-2@qwertysystem.net`: Active; penugasan seperti di atas; sedikitnya satu entri Tab Changelog dari seed Changelog sebelum pencabutan (target TC-FA-SU-943).
- Principal Automation (Pre-setup #12) memicu perubahan di Global Settings (App Access, identitas, status aktif, email, Custom Field) lewat sesi API; kemampuan ini disediakan tim FE (S-13). Langkah pemicunya ditulis "... hingga ... tersimpan" (R-20) dan bukan konteks UI kedua, sehingga tidak memakai `P-2`.
- Kemampuan mail-catcher untuk mengambil tautan aktivasi pengguna baru (TC-FA-SU-941 berautomation `Manual Only — (c)` karena tautan aktivasi ada di inbox email), disediakan tim FE; jam server dan jam browser sinkron karena Last Updated dibandingkan dengan waktu aksi (toleransi satu menit, S-12).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`). Pengguna milik spec dihapus di hook `after`.

## Test Steps

### TC-FA-SU-942: Pencabutan App Access FAMS di Global Settings: pengguna hilang dari User List; penugasan Transaction Role tetap tersimpan, penugasan FAMS lainnya dibersihkan

1. Ketik Search `Wawan Setiawan {runId}-305`, tekan Enter, klik nama Wawan Setiawan {runId}-305, lalu catat URL Detail
2. Principal Automation mencabut App Access FAMS dari Wawan Setiawan {runId}-305 di Global Settings hingga pencabutan tersimpan
3. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User
4. Ketik Search `Wawan Setiawan {runId}-305`, tekan Enter
5. Verifikasi empty state `No results found` tampil (pengguna hilang dari User List dan Search tanpa muat ulang manual)
6. Buka URL Detail Wawan Setiawan {runId}-305 yang dicatat
7. Verifikasi toast "This user is no longer available." tampil
8. Verifikasi aktor kembali ke User List yang di-refresh
9. Buka Settings > Role & Permission > Detail Role Manage files
10. Verifikasi daftar pemegang peran Manage files memuat sedikitnya satu pengguna lain (pembanding)
11. Verifikasi Wawan Setiawan {runId}-305 tidak tercantum sebagai pemegang peran Manage files

### TC-FA-SU-943: Pemberian ulang App Access setelah pencabutan diperlakukan seperti pengguna baru tanpa pemulihan wewenang lama

12. Catat jumlah entri Tab Changelog Wawan Setiawan 2 {runId}-305 sebagai baseline (riwayat lama)
13. Principal Automation mencabut lalu memberi kembali App Access FAMS pada Wawan Setiawan 2 {runId}-305 di Global Settings hingga keduanya tersimpan
14. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User dan Search `Wawan Setiawan 2 {runId}-305`, tekan Enter
15. Verifikasi kolom Role baris Wawan Setiawan 2 {runId}-305 `0 roles`
16. Verifikasi sakelar Active baris Wawan Setiawan 2 {runId}-305 ON
17. Verifikasi kolom Home Group baris Wawan Setiawan 2 {runId}-305 kosong (`—`)
18. Klik nama Wawan Setiawan 2 {runId}-305 lalu buka Tab Role
19. Verifikasi tingkat akses Wawan Setiawan 2 {runId}-305 `—` (User Type `Basic`)
20. Verifikasi Tab Role tidak memuat penugasan Global Role, Group Role, dan Transaction Role lama
21. Buka Tab Changelog, muat ulang sampai halaman termuat
22. Verifikasi jumlah entri Tab Changelog Wawan Setiawan 2 {runId}-305 sama dengan baseline (riwayat lama tetap tersimpan)

### TC-FA-SU-941: Pemberian App Access FAMS di Global Settings: pengguna tampil di User List tanpa peran dengan sakelar ON dan tanpa entri log

23. Catat jumlah entri ber-Name `Pengguna Baru {runId}-305` pada Tab System Log aktor dan Activity Log serta jumlah entri ber-User Name itu pada Modal Combined Changelog sebagai baseline
24. Principal Automation memberi App Access FAMS kepada Pengguna Baru {runId}-305 di Global Settings > User hingga App Access tersimpan
25. Catat waktu sesudah App Access tersimpan, lalu buka Fixed Asset > Settings > User dan Search `Pengguna Baru {runId}-305`, tekan Enter
26. Verifikasi sakelar Active baris Pengguna Baru {runId}-305 ON
27. Verifikasi kolom Role baris Pengguna Baru {runId}-305 `0 roles`
28. Verifikasi badge `Pending Activation` tampil pada baris Pengguna Baru {runId}-305
29. Verifikasi kolom Modified By baris Pengguna Baru {runId}-305 `System`
30. Verifikasi kolom Last Updated baris Pengguna Baru {runId}-305 sama dengan waktu pemberian App Access (toleransi satu menit)
31. Klik nama Pengguna Baru {runId}-305 untuk membuka Detail
32. Verifikasi tingkat akses kosong (User Type `Basic`)
33. Verifikasi banner tingkat akses tidak tampil
34. Buka Tab Changelog Pengguna Baru {runId}-305
35. Verifikasi header kolom Tab Changelog tampil
36. Verifikasi jumlah entri Tab Changelog Pengguna Baru {runId}-305 nol
37. Buka Tab System Log aktor dan cari Name `Pengguna Baru {runId}-305`
38. Verifikasi header kolom Tab System Log tampil
39. Verifikasi jumlah entri ber-Name Pengguna Baru {runId}-305 pada Tab System Log sama dengan baseline
40. Buka Activity Log dan cari Name `Pengguna Baru {runId}-305`
41. Verifikasi header kolom Activity Log tampil
42. Verifikasi jumlah entri ber-Name Pengguna Baru {runId}-305 pada Activity Log sama dengan baseline
43. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog dan cari User Name `Pengguna Baru {runId}-305`
44. Verifikasi jumlah entri ber-User Name Pengguna Baru {runId}-305 pada Modal Combined Changelog sama dengan baseline
45. Tutup Modal Combined Changelog dengan `[✕]`
46. Ambil tautan aktivasi Pengguna Baru {runId}-305 dari inbox lewat mail-catcher lalu aktivasi akun
47. Ganti akun: klik Logout pada akun saat ini
48. Login sebagai Pengguna Baru {runId}-305 (kredensial disediakan tim FE)
49. Verifikasi pengguna diarahkan ke halaman My Asset
50. Verifikasi pengguna tidak memiliki menu administratif lain

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-942 dan TC-FA-SU-943 (mencabut App Access) dikerjakan sebelum TC-FA-SU-941, karena TC-FA-SU-941 berakhir pada akun pengguna baru (ganti akun terakhir; sesi dipulihkan hook `after`, S-07).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 1, 3, 9, 14, 18, 21, 25, 31, 45, 47, 48; langkah baseline jumlah entri (S-12): 12, 23. Langkah 1, 14, dan 25 juga Search untuk menemukan baris target (R-16); langkah 47 dan 48 adalah ganti akun eksplisit.
- Alasan di atas sekitar 35 langkah: seluruh TC satu topik (refleksi App Access Global Settings pada User List dan surface log), tiap TC memakai pengguna milik spec, dan kegagalan satu TC tidak membuat TC lain kehilangan makna; langkah baca-log berpola tidak dihitung menurut bagian 3 prinsip 13 (Smell): 11 dari 50 langkah, sisa 39 langkah.
- Klausa "tanpa entri log" TC-FA-SU-941 ditulis sebagai asersi jumlah dengan baseline (S-12) dengan anchor positif (pengguna sudah tampil di User List dan header kolom surface termuat), bukan asersi absence kelas g (bagian 3 prinsip 13, "Asersi jumlah atau state"); langkah baca-log berpola tidak dihitung menurut Smell: 11 dari 50 langkah.
- Pengguna milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-305` (S-06); data dinamis `Pengguna Baru` tidak ditentukan namanya oleh TC.
- Temuan untuk QA (S-15):
  - TC-FA-SU-942 butir a menyebut Filter dan Download, dan butir b menyebut login FAMS diblokir, tetapi Langkah Uji hanya memuat Search, URL Detail, dan Detail Role; spec mengasersi yang punya langkah. Butir c (penugasan Global Role, Group Role, tingkat akses, Group Manager, Home Group dibersihkan; baris Transaction Role termasuk baris pola tier tetap tersimpan sesuai `E-FARP-49`; riwayat Changelog tetap tersimpan) hanya teramati lewat Detail Role Manage files (Group Role); sisanya, termasuk baris Transaction Role yang tetap tersimpan, tidak punya langkah observasi (Detail pengguna tidak dapat dibuka setelah pencabutan) dan tidak diasersi, dan Post Condition tidak punya langkah observasi.
  - TC-FA-SU-943 butir b (penugasan lama tidak dipulihkan, riwayat Changelog lama tetap tersimpan) memerlukan riwayat awal; TC tidak menyebut seed riwayat Wawan Setiawan, jadi spec mensyaratkannya di Prerequisites.
  - TC-FA-SU-941 menyebut Last Updated "sama dengan waktu pemberian App Access" tanpa toleransi; spec memakai toleransi satu menit (S-12). Butir d memerlukan password pengguna baru dan inbox email yang disediakan tim FE; Post Condition butir b (tidak ada entri log) sudah menjadi butir c.
  - Hint `g` TC-FA-SU-941 (asersi absence) ditulis sebagai asersi jumlah dengan baseline di spec ini; rujukan silang ke spec absence kelas g diputuskan pemilik proses.
