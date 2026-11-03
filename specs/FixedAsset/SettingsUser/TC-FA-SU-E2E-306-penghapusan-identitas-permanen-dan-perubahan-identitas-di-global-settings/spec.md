---
id: TC-FA-SU-E2E-306-penghapusan-identitas-permanen-dan-perubahan-identitas-di-global-settings
title: "Penghapusan Identitas Permanen dan Perubahan Identitas di Global Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-944
  - TC-FA-SU-945
coverage:
  web: automated
---

# Penghapusan Identitas Permanen dan Perubahan Identitas di Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan Global Settings (#38). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Putri Anggraeni {runId}-306`, email `putri.anggraeni+{runId}-306@qwertysystem.net`: Active; Group Role Manage files pada Finance & Accounting dan Home Group Finance & Accounting; sedikitnya satu entri Modal Combined Changelog dari seed Changelog (target TC-FA-SU-944).
  - `Budi Santoso {runId}-306`, email `budi.santoso+{runId}-306@qwertysystem.net`: Active; Position Finance Manager; Foto Profil terpasang di Global Settings (target TC-FA-SU-945).
- Principal Automation (Pre-setup #12) memicu perubahan di Global Settings (App Access, identitas, status aktif, email, Custom Field) lewat sesi API; kemampuan ini disediakan tim FE (S-13). Langkah pemicunya ditulis "... hingga ... tersimpan" (R-20) dan bukan konteks UI kedua, sehingga tidak memakai `P-2`.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`). Penghapusan identitas permanen TC-FA-SU-944 dikerjakan terakhir.

## Test Steps

### TC-FA-SU-945: Perubahan identitas di Global Settings tampil di User List dan Detail tanpa jalur edit lokal

1. Catat jumlah entri Tab Changelog Budi Santoso {runId}-306 sebagai baseline
2. Principal Automation mengubah Position Budi Santoso {runId}-306 menjadi `Finance Director` di Global Settings hingga perubahan tersimpan
3. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User dan Search `Budi Santoso {runId}-306`, tekan Enter
4. Verifikasi kolom Position baris Budi Santoso {runId}-306 `Finance Director`
5. Klik nama Budi Santoso {runId}-306 untuk membuka Detail
6. Verifikasi header Detail menampilkan Position `Finance Director`
7. Principal Automation menghapus Foto Profil Budi Santoso {runId}-306 di Global Settings hingga perubahan tersimpan
8. Tunggu aksi selesai, lalu buka ulang Detail Budi Santoso {runId}-306
9. Verifikasi header Detail menampilkan avatar inisial sebagai fallback foto
10. Buka Tab Changelog
11. Verifikasi header kolom Tab Changelog tampil
12. Verifikasi jumlah entri Tab Changelog Budi Santoso {runId}-306 sama dengan baseline (perubahan identitas tidak menulis entri di modul ini)

### TC-FA-SU-944: Penghapusan identitas permanen di Global Settings: seluruh data sisi FAMS dihapus tanpa salinan lokal

13. Catat jumlah entri pada Modal Combined Changelog ber-User Name `Putri Anggraeni {runId}-306` sebagai baseline
14. Principal Automation menghapus identitas Putri Anggraeni {runId}-306 secara permanen di Global Settings hingga penghapusan tersimpan
15. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User dan Search `Putri Anggraeni {runId}-306`, tekan Enter
16. Verifikasi empty state `No results found` tampil (pengguna hilang dari User List)
17. Buka Settings > Role & Permission > Detail Role Manage files
18. Verifikasi daftar pemegang peran Manage files memuat sedikitnya satu pengguna lain (pembanding)
19. Verifikasi Putri Anggraeni {runId}-306 tidak tercantum sebagai pemegang peran Manage files
20. Buka Fixed Asset > Settings > User, buka Modal Combined Changelog, dan buka filter User Name
21. Verifikasi filter User Name memuat opsi pengguna lain (pembanding)
22. Verifikasi filter User Name tidak memuat opsi `Putri Anggraeni {runId}-306`
23. Tutup filter lalu tutup Modal Combined Changelog dengan `[✕]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-945 dikerjakan sebelum TC-FA-SU-944 karena TC-FA-SU-944 menghapus data (S-10).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 3, 5, 8, 10, 15, 17, 20, 23; langkah baseline jumlah entri (S-12): 1, 13. Langkah 3 dan 15 juga Search untuk menemukan baris target (R-16).
- Klausa "tidak ada entri log" TC-FA-SU-945 ditulis sebagai asersi jumlah dengan baseline dan anchor header kolom (S-12), bukan asersi absence kelas g.
- Pengguna milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-306` (S-06).
- Temuan untuk QA (S-15):
  - TC-FA-SU-945 butir a menyebut Nama, Email, Position, Division, Employee ID, dan Foto Profil, tetapi Langkah Uji hanya mengubah Position dan Foto Profil; spec mengasersi dua perubahan itu. Langkah "buka ulang Detail" TC-FA-SU-945 tidak menyebut kolom foto di User List; spec mengasersi avatar fallback di header Detail.
  - TC-FA-SU-944 butir a menyebut seluruh baris penugasan terhapus dan butir b "tidak ada salinan data identitas di Detail maupun log aktif", tetapi Langkah Uji hanya memuat Search dan Detail Role Manage files; spec mengasersi Search, Detail Role Manage files, dan opsi filter User Name (tafsiran "log aktif"), dan menyatakan tafsiran itu di sini. Detail pengguna terhapus tidak dapat dibuka sehingga tidak diasersi.
