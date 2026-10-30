---
id: TC-GS-UCF-E2E-069-pencatatan-snapshot-nama-lama-dan-aktor-dihapus
title: "Pencatatan Snapshot: Entri Log Lama Tidak Berubah Setelah Rename Kedua, Name System Log Tidak Berubah, dan Modified By Tetap Menampilkan Aktor yang Sudah Dihapus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-289
  - TC-GS-UCF-554
  - TC-GS-UCF-555
coverage:
  web: automated
---

# Pencatatan Snapshot: Entri Log Lama Tidak Berubah Setelah Rename Kedua, Name System Log Tidak Berubah, dan Modified By Tetap Menampilkan Aktor yang Sudah Dihapus

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Seluruh aksi UI dan seeding riwayat TC-GS-UCF-289 dan TC-GS-UCF-554 dilakukan Sari Dewi, sehingga entri System Log berada di Detail Sari Dewi. Password tidak ditulis di spec atau fixture.
- Aktor TC-GS-UCF-555: Total Control Client A Candra Wibowo (Modified By `Candra W`) `totalControlTemp_automated_qaTeam1@qwertysystem.net` (Pre-setup TC; akun sementara, fixture baru), hanya sebagai aktor seeding `Snap Actor Probe` di hook `before` (login atau sesi per aktor disediakan tim FE/BE dengan `Spectra.env.GS_CANDRA_TC_PASSWORD`, env baru). Akun ini dihapus oleh TC-GS-UCF-555 sehingga tim FE menyediakan ulang akun ini per run. Spec tidak login sebagai Candra Wibowo.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field. Langkah yang membuka ulang halaman itu berfungsi sebagai pemulihan state sesudah System Log, Activity Log, atau User List.
- Data Pre-setup: tidak ada yang dipakai selain akun Candra Wibowo yang dihapus oleh TC-GS-UCF-555 (akun sementara milik spec ini, bukan akun bersama).
- Data Dinamis (nama bersuffix `{runId}-069`; fixture baru `Fixture.customFieldUser.logSnapshot069`):
  - Di-seed lewat API oleh Sari Dewi di hook `before` (precondition TC-GS-UCF-289, tidak diasersi satu per satu selain di langkah verifikasi): riwayat `Edit Meta {runId}-069` (Create), di-rename menjadi `Edit Meta {runId}-069 Renamed`, lalu menjadi `Edit Meta {runId}-069 Final` (Text, Placeholder kosong, nilai User Rahmat Hidayat = `Alpha Value`). Nama dirancang berawalan sama supaya satu Search `Edit Meta {runId}-069` mencakup seluruh entri.
  - Di-seed lewat aktor Candra Wibowo di hook `before`: `Snap Actor Probe {runId}-069` (Text), satu-satunya perubahan oleh Candra Wibowo.
  - Dibuat dan diubah lewat UI oleh spec: `Name Snap {runId}-069 Probe` dibuat (TC-GS-UCF-554), lalu di-rename menjadi `Name Snap {runId}-069 Renamed`; `Edit Meta {runId}-069 Final` di-rename menjadi `Edit Meta {runId}-069 Third` (TC-GS-UCF-289).
  - Entri Changelog, System Log, dan Activity Log bersifat audit trail permanen dan tidak dibersihkan; asersi memakai nama bersuffix unik per run.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Custom Field bersuffix `{runId}-069` yang masih ada (`Edit Meta {runId}-069 Third`, `Name Snap {runId}-069 Renamed`, `Snap Actor Probe {runId}-069`).
- Setup Column Modal Changelog: konfigurasi default; hook `beforeEach` membersihkan cache browser.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: seeding Custom Field dan nilai User lewat API dengan aktor tertentu (Sari Dewi, Candra Wibowo); Search pada Modal Changelog, tab System Log di Detail User, dan Activity Log tab User Action (kolom pencarian tidak dijelaskan di TC; lihat Temuan untuk QA); Search dan Delete user pada User List.
- State global: tidak ada yang diubah selain flag Guided Tooltip; akun Candra Wibowo dihapus (akun sementara, dipulihkan tim FE per run).

## Test Steps

### TC-GS-UCF-289: Entri log lama tidak berubah setelah rename kedua

1. Ketik Search `Edit Meta {runId}-069 Final` pada tabel utama, tekan Enter
2. Klik `⋯` pada baris `Edit Meta {runId}-069 Final`, pilih `Edit`
3. Ubah Field Name menjadi `Edit Meta {runId}-069 Third`
4. Klik `[Save]`
5. Tunggu aksi selesai (modal tertutup)
6. Klik icon Changelog
7. Ketik Search `Edit Meta {runId}-069`, tekan Enter
8. Verifikasi Changelog: entri Create tetap memuat nama awal `Edit Meta {runId}-069`
9. Verifikasi Changelog: entri Edit pertama tetap Old Value `Edit Meta {runId}-069`, New Value `Edit Meta {runId}-069 Renamed`
10. Verifikasi Changelog: entri Edit kedua tetap Old Value `Edit Meta {runId}-069 Renamed`, New Value `Edit Meta {runId}-069 Final`
11. Verifikasi Changelog: entri baru Old Value `Edit Meta {runId}-069 Final`, New Value `Edit Meta {runId}-069 Third`
12. Klik `[✕]`
13. Buka Global Settings > User > Detail Sari Dewi > tab System Log
14. Ketik Search `Edit Meta {runId}-069`, tekan Enter
15. Verifikasi System Log Sari Dewi: entri Edit Field Name tetap Old Value `Edit Meta {runId}-069`, New Value `Edit Meta {runId}-069 Renamed`
16. Verifikasi System Log Sari Dewi: entri Edit Field Name tetap Old Value `Edit Meta {runId}-069 Renamed`, New Value `Edit Meta {runId}-069 Final`
17. Verifikasi System Log Sari Dewi: entri baru Old Value `Edit Meta {runId}-069 Final`, New Value `Edit Meta {runId}-069 Third`
18. Buka Global Settings > Activity Log > tab User Action
19. Ketik Search `Edit Meta {runId}-069`, tekan Enter
20. Verifikasi Activity Log: entri Edit Field Name (Modified By `Sari D`) tetap Old Value `Edit Meta {runId}-069`, New Value `Edit Meta {runId}-069 Renamed`
21. Verifikasi Activity Log: entri Edit Field Name (Modified By `Sari D`) tetap Old Value `Edit Meta {runId}-069 Renamed`, New Value `Edit Meta {runId}-069 Final`
22. Verifikasi Activity Log: entri Edit Field Name (Modified By `Sari D`) Old Value `Edit Meta {runId}-069 Final`, New Value `Edit Meta {runId}-069 Third`
23. Buka Global Settings > User > Custom Field

### TC-GS-UCF-554: Name pada entri System Log lama tidak berubah setelah Custom Field di-rename

24. Klik `[+ Custom Field]`
25. Isi Field Name `Name Snap {runId}-069 Probe`
26. Pilih Data Type `Text`
27. Klik `[Submit]`
28. Verifikasi toast sukses: "Success, custom field has been created."
29. Ketik Search `Name Snap {runId}-069 Probe`, tekan Enter
30. Klik `⋯` pada baris `Name Snap {runId}-069 Probe`, pilih `Edit`
31. Ubah Field Name menjadi `Name Snap {runId}-069 Renamed`
32. Klik `[Save]`
33. Verifikasi toast sukses: "Success, custom field has been updated."
34. Buka Global Settings > User > Detail Sari Dewi > tab System Log
35. Ketik Search `Name Snap {runId}-069`, tekan Enter
36. Verifikasi System Log Sari Dewi memuat entri Create (Object `Custom Field`) dengan Name `Name Snap {runId}-069 Probe`
37. Verifikasi Name entri Create tidak berubah menjadi `Name Snap {runId}-069 Renamed`
38. Verifikasi System Log Sari Dewi memuat entri Edit dengan Old Value `Name Snap {runId}-069 Probe`, New Value `Name Snap {runId}-069 Renamed`
39. Buka Global Settings > User > Custom Field

### TC-GS-UCF-555: Modified By tetap menampilkan nama aktor saat aksi setelah aktor dihapus

40. Klik icon Changelog
41. Ketik Search `Snap Actor Probe {runId}-069`, tekan Enter
42. Verifikasi Changelog: entri Create `Snap Actor Probe {runId}-069` dengan Modified By `Candra W`
43. Klik `[✕]`
44. Buka Global Settings > User > User List (sub-tab Login User)
45. Ketik Search `Candra Wibowo`, tekan Enter
46. Klik `⋯` pada baris Candra Wibowo, pilih `Delete`
47. Klik `[Delete]` pada dialog
48. Verifikasi toast sukses: "Success, user has been deleted."
49. Buka Global Settings > User > Custom Field
50. Klik icon Changelog
51. Ketik Search `Snap Actor Probe {runId}-069`, tekan Enter
52. Verifikasi Changelog: entri Create `Snap Actor Probe {runId}-069` tetap dengan Modified By `Candra W`
53. Klik `[✕]`
54. Buka Global Settings > Activity Log > tab User Action
55. Ketik Search `Snap Actor Probe {runId}-069`, tekan Enter
56. Verifikasi Activity Log memuat entri Create dengan Name `Snap Actor Probe {runId}-069` dan Modified By `Candra W`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 289, 554, 555. Urutan menyimpang dari urutan TC sumber: aksi yang menghapus data (Delete user Candra Wibowo pada TC-GS-UCF-555) ditaruh paling akhir (bagian 3 prinsip 5).
- Langkah penghubung (aksi tanpa `Verifikasi`): pengisian Search tabel utama, Search pada Changelog, System Log, dan Activity Log, penutupan Modal Changelog lewat `[✕]` (tanpa dialog karena tidak ada form), pembukaan ulang Global Settings > User > Custom Field sebagai pemulihan state, pembukaan User List, dan langkah "Tunggu aksi selesai (modal tertutup)" sesudah `[Save]` pada TC-GS-UCF-289 yang hasilnya tidak diasersi langsung dan langkah berikutnya berpindah surface (bagian 8b butir 8). Pada TC-GS-UCF-554 dan 555 toast sukses diasersi sehingga tanpa langkah tunggu.
- TC-GS-UCF-555 langkah 1 TC ("catat Modified By entri Create, lalu tutup modal") ditulis sebagai `Verifikasi` Modified By `Candra W` karena Expected a menetapkan nilainya.
- Spec melewati sekitar 35 langkah (56 langkah). Sebagian besar blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log). Seluruhnya satu kelas (pencatatan snapshot), tiap blok memakai field bersuffix sendiri sehingga tetap bermakna bila blok lain gagal.
- Temuan untuk QA:
  - TC-GS-UCF-289 precondition mengacu rename pertama (TC-GS-UCF-95), rename kedua (TC-GS-UCF-99), dan field Pre-setup D-23 (`Edit Meta Final`) dari TC lain; spec membuat riwayat itu sendiri lewat seeding API oleh Sari Dewi (mekanisme seeding riwayat dan aktor disediakan tim FE/BE). Nama field bersuffix diubah menjadi bentuk `Edit Meta {runId}-069 Renamed` (nama dirancang berawalan sama) agar Search satu kali mencakup seluruh entri.
  - TC-GS-UCF-289 Expected e menyebut "aktor ketiga rename" sementara precondition menyatakan seluruh rename dilakukan Sari Dewi; spec memakai Sari Dewi untuk seluruh riwayat.
  - Mekanisme pencarian pada tab System Log dan Activity Log, serta kolom Object dan Name, tidak dijelaskan di TC (spec memakai Search atas nama bersuffix).
  - TC-GS-UCF-555 menyebut `Candra Wibowo` sebagai akun Pre-setup sementara yang dihapus oleh TC; env var password aktor seeding belum ditetapkan. Pencarian `Candra Wibowo` pada User List bergantung pada nama tampil yang unik.
  - TC-GS-UCF-555 Post Condition (Candra Wibowo terhapus) tidak punya langkah observasi tambahan.
  - TC-GS-UCF-554 Expected b dan c tidak menyebut Name entri Edit; spec hanya mengasersi Old Value dan New Value entri Edit.
