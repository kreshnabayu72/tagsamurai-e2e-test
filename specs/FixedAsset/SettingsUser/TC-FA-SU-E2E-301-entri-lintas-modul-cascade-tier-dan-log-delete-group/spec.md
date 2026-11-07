---
id: TC-FA-SU-E2E-301-entri-lintas-modul-cascade-tier-dan-log-delete-group
title: "Entri Lintas Modul, Cascade Tier, dan Log Delete Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-927
  - TC-FA-SU-928
  - TC-FA-SU-929
  - TC-FA-SU-930
coverage:
  web: automated
---

# Entri Lintas Modul, Cascade Tier, dan Log Delete Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Default User Ahmad Dahlan (Pre-setup #2), `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini (TC-FA-SU-928 beraktor Default User); halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Akun aktor kedua untuk TC-FA-SU-927, TC-FA-SU-929, dan TC-FA-SU-930: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`; ganti akun dengan langkah eksplisit 11 dan 12, dan hook `after` mengembalikan sesi ke akun default suite (S-07).
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23), dan Changelog (#27). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Gita Permata {runId}-301`, email `gita.permata+{runId}-301@qwertysystem.net`: Active; Global Role Import Data dan Manage accounting; Group Role Manage group pada Finance & Accounting; tanpa tingkat akses (target TC-FA-SU-927).
  - `Lina Marlina {runId}-301`, email `lina.marlina+{runId}-301@qwertysystem.net`: Active; tingkat akses Total Control (target TC-FA-SU-928).
  - `Gita Permata {runId}-301-2`, email `gita.permata+{runId}-301-2@qwertysystem.net`: Active; Global Role Import Data dan Manage accounting; Group Role Manage group pada Finance & Accounting; tanpa tingkat akses (target TC-FA-SU-929).
  - Grup `IT Infrastructure {runId}-301` (milik spec, dihapus oleh TC-FA-SU-930), Oscar Pranata (`Oscar Pranata {runId}-301`, email `oscar.pranata+{runId}-301@qwertysystem.net`): Group Manager pada grup itu, dan Indra Wijaya (`Indra Wijaya {runId}-301`, email `indra.wijaya+{runId}-301@qwertysystem.net`): Group Role dan Transaction Role pada grup itu.
- Kemampuan Principal Automation (Pre-setup #12) untuk mengubah tingkat akses dan Group Manager lewat Settings > Role & Permission, dan kemampuan baca notifikasi in-app pengguna target (Oscar Pranata): disediakan tim FE/BE (langkah UI Role & Permission tidak diuraikan TC).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Jendela absence notifikasi in-app (bagian 6 konvensi, 8b.11): langkah `Tunggu 5 detik tanpa memuat ulang halaman` (langkah 61) ditaruh sesudah anchor pembanding dan sebelum asersi absence notifikasi TC-FA-SU-930.
- Tidak ada intercept, jam server, atau klien HTTP. State global: pohon grup (grup milik spec dihapus oleh TC-FA-SU-930, dikerjakan terakhir); suite berjalan serial (`parallel: false`). Grup milik spec dihapus lewat seed API di hook `after` bila TC-FA-SU-930 belum menghapusnya.

## Test Steps

### TC-FA-SU-928: Penggantian tingkat akses Total Control ke Read Only dari Role & Permission dicatat dua entri Remove lalu Assign

1. Catat jumlah entri Action `Remove` Object `Total Control` dan Action `Assign` Object `Read Only` pada Tab Changelog Lina Marlina {runId}-301, Tab System Log aktor, dan Activity Log sebagai baseline
2. Di Settings > Role & Permission, ubah tingkat akses Lina Marlina {runId}-301 dari Total Control ke Read Only
3. Tunggu aksi selesai
4. Buka Fixed Asset > Settings > User, cari Lina Marlina {runId}-301, klik nama, lalu buka Tab Changelog, muat ulang sampai entri tampil
5. Verifikasi Tab Changelog memuat berurutan `Remove` (Old Value `Total Control`, New Value `—`) lalu `Assign` (Old Value `—`, New Value `Read Only`) dengan Field `Access Level`
6. Buka Tab System Log aktor dan cari Name `Lina Marlina {runId}-301`, muat ulang sampai entri tampil
7. Verifikasi Tab System Log memuat berurutan `Remove` Object `Total Control` (Old Value `Total Control`, New Value `—`) lalu `Assign` Object `Read Only` (Old Value `—`, New Value `Read Only`)
8. Buka Activity Log dan cari Name `Lina Marlina {runId}-301`, muat ulang sampai entri tampil
9. Verifikasi Activity Log memuat pasangan entri yang sama
10. Verifikasi jumlah entri `Assign` dengan Old Value berisi tingkat akses lama (`Total Control`) pada Tab Changelog, Tab System Log, dan Activity Log sama dengan baseline
11. Ganti akun: klik Logout pada akun saat ini
12. Login sebagai Lina Marlina (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`) lalu buka Fixed Asset > Settings > User

### TC-FA-SU-927: Entri dari Settings > Role & Permission tampil di Tab Changelog dan System Log Settings > User dengan Object yang sama

13. Catat jumlah entri Field `Access Level` dan Field `Group Manager — Finance & Accounting` pada Tab Changelog Gita Permata {runId}-301 dan Tab System Log aktor sebagai baseline
14. Di Settings > Role & Permission, tetapkan Gita Permata {runId}-301 sebagai Total Control
15. Di Settings > Role & Permission, tetapkan Gita Permata {runId}-301 sebagai Read Only
16. Di Settings > Role & Permission, lepaskan tingkat akses Gita Permata {runId}-301
17. Di Settings > Role & Permission, tetapkan Gita Permata {runId}-301 sebagai Group Manager pada Finance & Accounting
18. Di Settings > Role & Permission, lepaskan Group Manager Finance & Accounting dari Gita Permata {runId}-301
19. Tunggu aksi selesai
20. Buka Fixed Asset > Settings > User, cari Gita Permata {runId}-301, klik nama, lalu buka Tab Changelog, muat ulang sampai entri tampil
21. Verifikasi Tab Changelog memuat entri `Assign` Field `Access Level` dengan Old Value `—` (atau `Read Only`) dan New Value `Total Control`
22. Verifikasi Tab Changelog memuat entri Remove Total Control serta Assign dan Remove Read Only dengan Field `Access Level`
23. Verifikasi Tab Changelog memuat entri Assign dan Remove Group Manager dengan Field `Group Manager — Finance & Accounting` dan nilai `Assigned` atau `—`
24. Verifikasi jumlah entri baru pada Tab Changelog bertambah tepat enam dari baseline (tidak ada entri ganda dari modul ini)
25. Buka Tab System Log aktor dan cari Name `Gita Permata {runId}-301`, muat ulang sampai entri tampil
26. Verifikasi Tab System Log memuat entri `Assign` Object `Total Control` Field `Access Level` dengan Old Value `—` (atau `Read Only`) dan New Value `Total Control`
27. Verifikasi Tab System Log memuat entri Remove Total Control serta Assign dan Remove Read Only dengan Object `Total Control` atau `Read Only` dan Field `Access Level`
28. Verifikasi Tab System Log memuat entri Assign dan Remove Group Manager dengan Object `Group Manager`, Field `Group Manager — Finance & Accounting`, dan nilai `Assigned` atau `—`
29. Verifikasi kolom Object entri-entri itu hanya bernilai `Total Control`, `Read Only`, dan `Group Manager`, tanpa penanda asal edit (Role & Permission atau Settings > User)

### TC-FA-SU-929: Entri cascade via Total Control atau Read Only hanya tampil di Modal Changelog User > Global Role dan Group Role

30. Catat jumlah entri `Assign` dan `Remove` Object `Total Control` pada Tab Changelog dan Modal Combined Changelog Gita Permata {runId}-301-2 sebagai baseline
31. Di Settings > Role & Permission, tetapkan Gita Permata {runId}-301-2 sebagai Total Control lalu lepaskan
32. Tunggu aksi selesai
33. Buka Fixed Asset > Settings > User, cari Gita Permata {runId}-301-2, klik nama, lalu buka Tab Role dan modal Changelog User > Global Role, muat ulang sampai entri tampil
34. Verifikasi modal Changelog User > Global Role memuat entri `Assign (via Total Control)` dan `Remove (via Total Control)` dengan Field `Access`
35. Tutup modal Changelog User > Global Role dengan `[✕]` lalu buka modal Changelog User > Group Role
36. Verifikasi modal Changelog User > Group Role memuat satu entri `Remove (via Total Control)` dengan Field `Manage group — Finance & Accounting`, Old Value `Assigned`, dan New Value `—`
37. Verifikasi modal Changelog User > Group Role tidak memuat entri `Assign (via Total Control)`
38. Tutup modal Changelog User > Group Role dengan `[✕]`, buka modal Changelog User > Transaction Role, dan muat ulang sampai riwayat tampil
39. Verifikasi modal Changelog User > Transaction Role tidak memuat entri `Assign (via Total Control)` maupun `Remove (via Total Control)`
40. Tutup modal Changelog User > Transaction Role dengan `[✕]` lalu buka Tab Changelog, muat ulang sampai entri tampil
41. Verifikasi Tab Changelog memuat entri `Assign` dan `Remove` Object `Total Control` (anchor entri tingkat akses)
42. Verifikasi Tab Changelog tidak memuat entri `Assign (via Total Control)` maupun `Remove (via Total Control)`
43. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog, cari User Name `Gita Permata {runId}-301-2`, muat ulang sampai entri tampil
44. Verifikasi Modal Combined Changelog memuat entri tingkat akses Gita Permata {runId}-301-2 (anchor) dan tidak memuat entri `Assign (via Total Control)` maupun `Remove (via Total Control)`
45. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-930: Log Delete Group menghasilkan tiga jenis entri Remove dengan pelaku admin yang menghapus grup

46. Catat jumlah entri Action `Remove` pada Tab Changelog Oscar Pranata {runId}-301 dan Indra Wijaya {runId}-301, Tab System Log aktor, dan Activity Log sebagai baseline
47. Hapus grup IT Infrastructure {runId}-301 di Settings > Groups
48. Tunggu aksi selesai (grup hilang dari daftar Settings > Groups)
49. Buka Fixed Asset > Settings > User, cari Oscar Pranata {runId}-301, klik nama, lalu buka Tab Changelog, muat ulang sampai entri tampil
50. Verifikasi Tab Changelog memuat entri `Remove` dengan Field `Group Manager — IT Infrastructure {runId}-301`, Old Value `Assigned`, New Value `—`, dan Modified By `Lina M`
51. Verifikasi tabel Tab Changelog tidak memuat kolom Object dan nama grup terbawa di Field (Object tidak ada)
52. Kembali ke User List, ganti isi kotak search dengan `Indra Wijaya {runId}-301`, tekan Enter, klik nama Indra Wijaya {runId}-301, lalu buka Tab Changelog, muat ulang sampai entri tampil
53. Verifikasi Tab Changelog memuat entri `Remove` per assignment Group Role dan Transaction Role pada grup IT Infrastructure {runId}-301 dengan Field membawa nama grup dan Modified By `Lina M`
54. Buka Tab System Log aktor, muat ulang sampai entri tampil
55. Verifikasi Tab System Log memuat entri `Remove` Object `Group Manager (Group Deleted)` dengan Field `Group Manager — IT Infrastructure {runId}-301`, Old Value `Assigned`, dan New Value `—`
56. Verifikasi Tab System Log memuat entri `Remove` Object `Group Role` dan entri `Remove` Object `Transaction Role` per assignment yang terlepas
57. Buka Activity Log, muat ulang sampai entri tampil
58. Verifikasi Activity Log memuat entri `Remove` Object `Group Manager (Group Deleted)`, `Group Role`, dan `Transaction Role` dengan Modified By `Lina M` (admin yang menghapus grup)
59. Buka panel notifikasi in-app Oscar Pranata {runId}-301 lewat kemampuan baca notifikasi
60. Verifikasi panel notifikasi Oscar Pranata {runId}-301 memuat sedikitnya satu notifikasi lain sebagai pembanding
61. Tunggu 5 detik tanpa memuat ulang halaman
62. Verifikasi panel notifikasi Oscar Pranata {runId}-301 tidak memuat notifikasi penghapusan grup IT Infrastructure {runId}-301

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-928 (aktor Default User) dikerjakan pertama dan TC-FA-SU-930 (menghapus grup) terakhir; TC-FA-SU-927 dan TC-FA-SU-929 memakai pengguna berbeda karena TC-FA-SU-929 mengubah Group Role target lewat cascade tingkat akses (S-10, S-06).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 3, 19, 32, 48, 61, 11, 12; langkah baseline jumlah entri (S-12): 1, 13, 30, 46. Langkah 11 dan 12 adalah ganti akun eksplisit.
- Alasan di atas sekitar 35 langkah: seluruh TC satu kelas (pencatatan pada tiga surface log, bukan kelas harness lain), tiap TC berdiri sendiri dengan pengguna dan baseline sendiri, dan kegagalan satu TC tidak membuat TC lain kehilangan makna. Langkah baca-log berpola (buka surface, muat ulang sampai entri tampil, `Verifikasi` kolom log, `Verifikasi` jumlah entri) tidak dihitung menurut bagian 3 prinsip 13 (Smell): 40 dari 62 langkah, sisa 22 langkah. Alasan kelas: seluruh TC mengasersi pencatatan peristiwa lintas modul pada surface log Settings > User.
- Asersi bahwa entri cascade tidak tampil di Tab Changelog, Modal Combined Changelog, dan modal Changelog User > Transaction Role (TC-FA-SU-929 butir c) adalah asersi scope exclusion dengan anchor positif entri tingkat akses pada surface yang sama, bukan asersi absence kelas g (bagian 3 prinsip 13 butir g). Klausa "tidak ada notifikasi" TC-FA-SU-930 butir d memakai pembanding notifikasi lain pada panel yang sama.
- Langkah 52 juga Search untuk menemukan baris target (R-16, 8b.13): kotak Search masih berisi nama Oscar Pranata dari langkah 49, sehingga ditulis "ganti isi kotak search" sesudah "Kembali ke User List" (8b.9).
- Pengguna dan grup milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-301` (S-06).
- Temuan untuk QA (S-15):
  - TC-FA-SU-927 butir a, b dan TC-FA-SU-928 butir a menyebut Object pada Tab Changelog, padahal Tab Changelog tidak memiliki kolom Object (TC-FA-SU-909 butir a dan TC-FA-SU-936). Spec mengasersi Action, Field, Old Value, dan New Value pada Tab Changelog dan Object pada Tab System Log dan Activity Log.
  - Langkah Uji TC-FA-SU-927 sampai TC-FA-SU-929 menyebut Settings > Role & Permission tanpa menguraikan langkah UI-nya; spec menuliskan satu aksi per peristiwa dan kemampuan teknisnya tercantum di Prerequisites. TC-FA-SU-927 butir d ("modul ini tidak menulis entri baru") tidak punya langkah observasi yang membedakan penulis; spec mengasersi jumlah entri baru tepat enam dan Object tanpa penanda asal edit.
  - TC-FA-SU-930 tidak menyebut pengguna mana yang memegang assignment Group Role dan Transaction Role pada IT Infrastructure selain Oscar Pranata (Group Manager); spec memakai Indra Wijaya (langkah Uji menyebutnya) dan nilai Field yang diasersi hanya yang disebut Expected. Butir d (tidak ada notifikasi) tidak punya anchor di TC; spec memakai notifikasi lain pada panel sebagai pembanding.
  - Post Condition TC-FA-SU-928 dan TC-FA-SU-930 tidak punya langkah observasi tambahan dan tidak diasersi.
