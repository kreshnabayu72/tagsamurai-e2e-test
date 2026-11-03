---
id: TC-FA-SU-E2E-304-log-tanpa-peristiwa-pembuatan-atau-penghapusan-dan-snapshot-immutable
title: "Log Tanpa Peristiwa Pembuatan atau Penghapusan dan Snapshot Immutable"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-938
  - TC-FA-SU-939
coverage:
  web: automated
---

# Log Tanpa Peristiwa Pembuatan atau Penghapusan dan Snapshot Immutable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), Changelog (#27), dan Global Settings (#38). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Pengguna Baru {runId}-304`, email `pengguna.baru+{runId}-304@qwertysystem.net`: identitas ada di Global Settings tanpa App Access FAMS (target TC-FA-SU-938).
  - `Budi Santoso {runId}-304`, email `budi.santoso+{runId}-304@qwertysystem.net`: Active; dipakai membuka Tab Changelog untuk dropdown filter Action (TC-FA-SU-938).
  - `Gita Permata {runId}-304`, email `gita.permata+{runId}-304@qwertysystem.net`: Active; sedikitnya satu entri Tab Changelog dari seed Changelog sebelum aksi (target TC-FA-SU-939); namanya diubah di Global Settings menjadi `Gita Permata Dewi {runId}-304`.
- Principal Automation (Pre-setup #12) memicu perubahan di Global Settings (App Access, identitas, status aktif, email, Custom Field) lewat sesi API; kemampuan ini disediakan tim FE (S-13). Langkah pemicunya ditulis "... hingga ... tersimpan" (R-20) dan bukan konteks UI kedua, sehingga tidak memakai `P-2`.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-938: Log tidak mengandung peristiwa pembuatan atau penghapusan pengguna

1. Catat jumlah entri pada Modal Combined Changelog sebagai baseline
2. Ketik Search `Budi Santoso {runId}-304`, tekan Enter, klik nama Budi Santoso {runId}-304, lalu buka Tab Changelog
3. Klik icon Filter lalu buka dropdown Action pada Tab Changelog
4. Verifikasi dropdown Action Tab Changelog memuat opsi `Activate` dan `Deactivate` (pembanding)
5. Verifikasi dropdown Action Tab Changelog tidak memuat `Create` maupun `Delete`
6. Tutup panel Filter lalu buka Tab System Log aktor, klik icon Filter, dan buka dropdown Action
7. Verifikasi dropdown Action Tab System Log memuat opsi `Activate` dan `Deactivate` (pembanding)
8. Verifikasi dropdown Action Tab System Log tidak memuat `Create` maupun `Delete`
9. Principal Automation memberi App Access FAMS kepada Pengguna Baru {runId}-304 di Global Settings > User hingga App Access tersimpan
10. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User dan Search `Pengguna Baru {runId}-304`, tekan Enter
11. Verifikasi baris Pengguna Baru {runId}-304 tampil di User List (pembanding bahwa pemberian App Access sudah diproses)
12. Buka Modal Combined Changelog, muat ulang sampai halaman termuat, lalu cari User Name `Pengguna Baru {runId}-304`
13. Verifikasi jumlah entri pada Modal Combined Changelog sama dengan baseline (pemberian App Access tidak menghasilkan entri di modul ini)
14. Verifikasi tidak ada entri ber-User Name `Pengguna Baru {runId}-304` pada Modal Combined Changelog
15. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-939: Entri log tetap tersimpan sebagai snapshot immutable setelah pengguna dinonaktifkan atau peran diubah

16. Ketik Search `Gita Permata {runId}-304`, tekan Enter, klik nama Gita Permata {runId}-304, lalu buka Tab Changelog
17. Catat isi entri Tab Changelog Gita Permata {runId}-304 (Date, Action, Field, Old Value, New Value) sebagai snapshot awal
18. Kembali ke User List lewat breadcrumb `User`, Search `Gita Permata {runId}-304`, tekan Enter
19. Klik sakelar Active pada baris Gita Permata {runId}-304, lalu klik `[Deactivate]` pada dialog `Deactivate User`
20. Tunggu aksi selesai, lalu buka Detail Gita Permata {runId}-304 > Tab Changelog dan muat ulang sampai entri Deactivate tampil
21. Verifikasi entri snapshot awal tidak berubah setelah Gita Permata {runId}-304 dinonaktifkan
22. Catat isi seluruh entri Tab Changelog Gita Permata {runId}-304 sebagai snapshot kedua
23. Principal Automation mengubah nama Gita Permata {runId}-304 di Global Settings menjadi `Gita Permata Dewi {runId}-304` hingga perubahan tersimpan
24. Tunggu aksi selesai, lalu buka ulang Detail pengguna (nama baru `Gita Permata Dewi {runId}-304`) > Tab Changelog
25. Verifikasi entri lama Tab Changelog tidak berubah setelah nama pengguna berubah
26. Verifikasi Old Value dan New Value entri lama sama dengan snapshot kedua

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 2, 6, 10, 12, 15, 16, 18, 20, 24; langkah baseline jumlah entri (S-12): 1, 17, 22. Langkah 2, 10, 16, dan 18 juga Search untuk menemukan baris target (R-16).
- Klausa "tidak memuat" TC-FA-SU-938 dan TC-FA-SU-939 ditulis sebagai asersi jumlah atau scope exclusion dengan anchor positif pada surface yang sama (opsi pembanding, atau baseline), bukan asersi absence kelas g (bagian 3 prinsip 13 butir g).
- Pengguna milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-304` (S-06); `Pengguna Baru` adalah data dinamis TC-FA-SU-938 yang namanya tidak ditentukan TC.
- Temuan untuk QA (S-15):
  - Langkah Uji TC-FA-SU-938 hanya menyebut dropdown filter Action pada Tab Changelog, sedangkan Expected butir a menyebut Tab Changelog dan System Log; spec membuka keduanya. TC tidak menyebut pengguna yang Tab Changelog-nya dibuka; spec memakai Budi Santoso milik spec.
  - TC-FA-SU-939 tidak menyebut isi entri awal Gita Permata; Pre-setup #27 memuat riwayat Budi Santoso. Spec mensyaratkan seed entri Tab Changelog milik Gita sebelum aksi supaya asersi snapshot bermakna; perubahan nama dilakukan Principal Automation dan nama barunya dipilih spec (TC tidak menyebut nilainya).
  - Post Condition TC-FA-SU-938 dan TC-FA-SU-939 tidak ada.
