---
id: TC-FA-SU-E2E-303-notifikasi-auto-revert-struktur-kolom-tiga-surface-log-dan-object-action-pendek
title: "Notifikasi Auto-Revert, Struktur Kolom Tiga Surface Log, dan Object Action Pendek"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-935
  - TC-FA-SU-936
  - TC-FA-SU-937
coverage:
  web: automated
---

# Notifikasi Auto-Revert, Struktur Kolom Tiga Surface Log, dan Object Action Pendek

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Akun aktor kedua untuk TC-FA-SU-935 dan TC-FA-SU-937: Default User Ahmad Dahlan (Pre-setup #2), `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`; ganti akun dengan langkah eksplisit 11 dan 12, dan hook `after` mengembalikan sesi ke akun default suite (S-07).
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), penugasan (#23), Changelog (#27), dan System Log (#28). Target TC-FA-SU-936 adalah Budi Santoso Pre-setup (hanya dibaca, tidak diubah). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Lina Marlina {runId}-303`, email `lina.marlina+{runId}-303@qwertysystem.net`: Active; tingkat akses Total Control; Global Role Manage accounting dengan Update tercentang (target Auto-Revert TC-FA-SU-935).
  - `Gita Permata {runId}-303`, email `gita.permata+{runId}-303@qwertysystem.net`: Active; tanpa aset aktif (target Deactivate TC-FA-SU-935).
  - `Lina Marlina {runId}-303-2`, email `lina.marlina+{runId}-303-2@qwertysystem.net`: Active; tingkat akses Total Control; Global Role Manage accounting dengan Update tercentang (target Auto-Revert TC-FA-SU-937).
  - `Gita Permata {runId}-303-2`, email `gita.permata+{runId}-303-2@qwertysystem.net`: Active; Home Group Finance & Accounting; tanpa Global Role Manage asset ID configuration (target Assign Global Role dan Edit Home Group TC-FA-SU-937).
  - `Doni Prasetyo {runId}-303-2`, email `doni.prasetyo+{runId}-303-2@qwertysystem.net`: Inactive (target Activate TC-FA-SU-937).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Kemampuan baca notifikasi in-app pengguna target (jumlah dan jenis notifikasi), disediakan tim FE/BE: pengguna milik spec tidak punya kredensial login, dan pengguna nonaktif tidak dapat login ke FAMS.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-936: Perbedaan struktur kolom tiga surface log

1. Ketik Search `Budi`, tekan Enter, klik nama Budi Santoso, lalu buka Tab Changelog
2. Verifikasi Tab Changelog memuat kolom `Date | Action | Field | Old Value | New Value | Modified By` tanpa kolom Object
3. Buka Tab Role > Sub-tab Global Role lalu buka modal Changelog User
4. Verifikasi modal Changelog User memuat kolom `Date | Action | Field | Old Value | New Value | Modified By` tanpa kolom Object
5. Tutup modal Changelog User dengan `[✕]` lalu buka Fixed Asset > Settings > User dan buka Modal Combined Changelog
6. Verifikasi Modal Combined Changelog memuat kolom `User Name | Date | Action | Field | Old Value | New Value | Modified By` tanpa kolom Object
7. Tutup Modal Combined Changelog dengan `[✕]` lalu buka Detail Budi Santoso > Tab System Log
8. Verifikasi Tab System Log memuat kolom `Date | Action | Object | Name | Field | Old Value | New Value` tanpa kolom Modified By
9. Buka Activity Log
10. Verifikasi Activity Log memuat kolom `Date | Action | Object | Name | Field | Old Value | New Value | Modified By`
11. Ganti akun: klik Logout pada akun saat ini
12. Login sebagai Ahmad Dahlan (`defaultUser_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_DU_PASSWORD`) lalu buka Fixed Asset > Settings > User

### TC-FA-SU-935: Notifikasi in-app view-only ke target saat Auto-Revert dan tidak ada notifikasi untuk Deactivate

13. Catat jumlah notifikasi in-app Lina Marlina {runId}-303 dan Gita Permata {runId}-303 sebagai baseline
14. Ketik Search `Lina Marlina {runId}-303`, tekan Enter, klik nama Lina Marlina {runId}-303, lalu buka Tab Role > Sub-tab Global Role
15. Hapus centang Update pada baris Manage accounting lalu klik `[Remove]` pada dialog (Auto-Revert Total Control)
16. Tunggu aksi selesai, lalu kembali ke User List lewat breadcrumb `User`
17. Ganti isi kotak search dengan `Gita Permata {runId}-303`, tekan Enter
18. Klik sakelar Active pada baris Gita Permata {runId}-303, lalu klik `[Deactivate]` pada dialog `Deactivate User`
19. Tunggu aksi selesai (dialog tertutup dan sakelar baris berpindah ke OFF)
20. Baca notifikasi in-app Lina Marlina {runId}-303 lewat kemampuan baca notifikasi
21. Verifikasi Lina Marlina {runId}-303 menerima satu notifikasi in-app view-only baru (jumlah bertambah satu dari baseline) untuk Auto-Revert Total Control
22. Baca notifikasi in-app Gita Permata {runId}-303 lewat kemampuan baca notifikasi
23. Verifikasi jumlah notifikasi in-app Gita Permata {runId}-303 sama dengan baseline (tidak ada notifikasi terpisah untuk Deactivate)

### TC-FA-SU-937: Action pendek dengan Object jenis peran konsisten di System Log dan Activity Log; peristiwa non-peran memakai Object Settings > User

24. Catat jumlah entri pada Activity Log sebagai baseline
25. Ganti isi kotak search dengan `Gita Permata {runId}-303-2`, tekan Enter, klik nama Gita Permata {runId}-303-2, lalu buka Tab Role > Sub-tab Global Role
26. Nyalakan switch pada baris Manage asset ID configuration (Assign Global Role)
27. Tunggu aksi selesai, lalu kembali ke User List lewat breadcrumb `User`
28. Ganti isi kotak search dengan `Lina Marlina {runId}-303-2`, tekan Enter, klik nama Lina Marlina {runId}-303-2, lalu buka Tab Role > Sub-tab Global Role
29. Hapus centang Update pada baris Manage accounting lalu klik `[Remove]` pada dialog (Auto-Revert Total Control)
30. Tunggu aksi selesai, lalu kembali ke User List lewat breadcrumb `User`
31. Ganti isi kotak search dengan `Doni Prasetyo {runId}-303-2`, tekan Enter
32. Klik sakelar Active pada baris Doni Prasetyo {runId}-303-2, lalu klik `[Activate]` pada dialog `Activate User` (Activate)
33. Tunggu aksi selesai (dialog tertutup dan sakelar baris berpindah ke ON)
34. Ganti isi kotak search dengan `Gita Permata {runId}-303-2`, tekan Enter
35. Klik ⋯ pada baris Gita Permata {runId}-303-2, klik `Edit Home Group`, klik node IT Infrastructure pada popup `Select Home Group`, lalu klik `[Select]` (Edit Home Group)
36. Tunggu aksi selesai (popup tertutup)
37. Buka Activity Log, muat ulang sampai entri tampil
38. Verifikasi jumlah entri Activity Log bertambah tepat empat dari baseline
39. Verifikasi entri Assign Global Role (Name `Gita Permata {runId}-303-2`) memakai Action `Assign` dan Object `Global Role`
40. Verifikasi entri Auto-Revert Total Control (Name `Lina Marlina {runId}-303-2`) memakai Action `Auto-Revert` dan Object `Total Control`
41. Verifikasi entri Activate (Name `Doni Prasetyo {runId}-303-2`) memakai Action `Activate` dan Object `Settings > User`
42. Verifikasi entri Edit Home Group (Name `Gita Permata {runId}-303-2`) memakai Action `Edit Home Group` dan Object `Settings > User`
43. Verifikasi kolom Action keempat entri itu tidak berisi nilai gabungan seperti `Assign Total Control`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-936 (aktor Total Control, pengguna Pre-setup dibaca) dikerjakan pertama sebagai screening, TC-FA-SU-935 dan TC-FA-SU-937 (aktor Default User) sesudah ganti akun (S-10, S-07).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 1, 3, 5, 7, 9, 14, 16, 17, 19, 25, 27, 28, 30, 31, 33, 34, 36, 11, 12; langkah baseline jumlah entri (S-12): 13, 24. Langkah 1, 14, 17, 25, 28, 31, dan 34 juga Search untuk menemukan baris target (R-16); langkah 11 dan 12 adalah ganti akun eksplisit.
- Alasan di atas sekitar 35 langkah: seluruh TC satu kelas (struktur dan pencatatan surface log), tiap TC berdiri sendiri dengan pengguna milik spec, dan kegagalan satu TC tidak membuat TC lain kehilangan makna. Langkah baca Activity Log TC-FA-SU-937 (buka surface, muat ulang sampai entri tampil, `Verifikasi` Action dan Object) adalah blok baca-log berpola dan tidak dihitung menurut bagian 3 prinsip 13 (Smell): 7 dari 43 langkah.
- TC-FA-SU-937 memakai tiga pengguna milik spec (satu per peristiwa) karena TC hanya menyebut Gita Permata dan Lina Marlina sebagai data uji sedangkan Activate membutuhkan pengguna Inactive; baris Activity Log dicari lewat Name bersuffix dan selisih jumlah entri tepat empat (S-12).
- Pengguna milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-303` (S-06).
- Temuan untuk QA (S-15):
  - TC-FA-SU-935 berautomation `Manual Only — (d)` karena notifikasi diamati pada sesi pengguna target; spec memakai kemampuan baca notifikasi in-app yang disediakan tim FE/BE (pengguna Inactive tidak dapat login ke FAMS) dan hanya mengasersi notifikasi diterima target (copy dimiliki PRD notification; Catatan TC).
  - TC-FA-SU-937 menyebut Gita Permata untuk Activate padahal Gita berstatus Active di Pre-setup; spec memakai pengguna Inactive terpisah untuk Activate. Expected butir a menyebut `Group Role`, `Transaction Role`, `Read Only`, `Group Manager`, `Group Manager (Group Deleted)` sebagai Object tetapi Langkah Uji hanya memicu Assign Global Role dan Auto-Revert Total Control; hanya dua Object itu yang diasersi.
  - TC-FA-SU-936 butir a menyebut Tab Changelog dan modal Changelog User memuat kolom yang sama; urutan kolom `User Name` pada Modal Combined Changelog (di depan atau di belakang) tidak dinyatakan TC dan diserahkan ke Page Object.
