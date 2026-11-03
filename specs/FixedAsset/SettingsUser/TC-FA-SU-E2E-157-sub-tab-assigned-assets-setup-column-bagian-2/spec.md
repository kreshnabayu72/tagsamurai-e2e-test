---
id: TC-FA-SU-E2E-157-sub-tab-assigned-assets-setup-column-bagian-2
title: "Sub-tab Assigned Assets: Setup Column (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-461
  - TC-FA-SU-462
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Setup Column (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#24): Detail Budi Santoso dengan Sub-tab Assigned Assets 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #24 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC (Asset ID dan Transaction ID hanya tertulis sebagian):

| Name | Asset ID | Transaction ID | Brand | Model / Type | PIC |
|---|---|---|---|---|---|
| `AC Split Ruang Kerja` | tidak tertulis | tidak tertulis | `Daikin` | `1PK` | `Ahmad D` |
| `Lemari Arsip` | tidak tertulis | tidak tertulis | `Lion` | `2 Pintu` | `Citra L` |
| `Meja Kerja Kepala Divisi` | tidak tertulis | `ASG-20260505` | `Modera` | `Executive` | `Ahmad D` |
| `Printer Multifungsi` | tidak tertulis | tidak tertulis | `Canon` | `PIXMA G3010` | `Citra L` |
| `Server Rack Mini` | `AST-02113` | tidak tertulis | `HP` | `ProLiant DL20` | `Eka W` (Eka Wulandari) |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).
- Tabel parameter "Kelompok Pin" (dipakai langkah 3 sampai 16):

| Kelompok | Kolom |
|---|---|
| 1 | `Photo`, `Name`, `Asset ID` |
| 2 | `Transaction ID`, `Brand`, `Model / Type` |
| 3 | `PIC` |

Maksimum tiga kolom di-pin sekaligus, sehingga kolom di-pin per kelompok dan di-unpin sebelum kelompok berikutnya.
- Kemampuan menghapus preferensi kolom Setup Column di browser (disediakan tim FE): dipakai sebagai langkah pemulihan dan di hook `after` untuk tabel yang konfigurasinya disimpan spec ini (bagian 4 konvensi). Konfigurasi kolom tersimpan per perangkat dan per tabel.
- Kemampuan teknis: viewport browser dipersempit agar tabel dapat di-scroll horizontal (disediakan tim FE).

## Test Steps

### TC-FA-SU-461: Pin dan unpin Setup Column Sub-tab Assigned Assets kelas Hideable (default tampil)

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
3. Untuk setiap baris tabel parameter "Kelompok Pin" (langkah 3 sampai 16): klik header kolom Actions (⋯)
4. Klik `Setup Column...`
5. Klik icon Pin pada tiap kolom kelompok itu
6. Klik `[Save]`
7. Scroll tabel secara horizontal
8. Verifikasi tiap kolom kelompok itu membeku di kiri saat tabel di-scroll horizontal
9. Tekan F5 pada halaman Detail
10. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
11. Verifikasi tiap kolom kelompok itu tetap membeku di kiri setelah F5
12. Klik header kolom Actions (⋯)
13. Klik `Setup Column...`
14. Klik icon Pin yang aktif pada tiap kolom kelompok itu untuk unpin
15. Klik `[Save]`
16. Verifikasi tiap kolom kelompok itu tidak lagi membeku saat tabel di-scroll horizontal
17. Klik header kolom Actions (⋯)
18. Klik `Setup Column...`
19. Klik icon Pin pada kolom `Photo`, `Name`, dan `Asset ID`
20. Hover icon Pin kolom `Transaction ID`
21. Verifikasi icon Pin kolom `Transaction ID` disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
22. Klik ✕ pada popup Setup Column untuk membuang perubahan
23. Pulihkan konfigurasi kolom tabel Assigned Assets: hapus preferensi kolom di browser
24. Tekan F5 pada halaman Detail
25. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets

### TC-FA-SU-462: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column Sub-tab Assigned Assets

26. Klik header kolom Actions (⋯)
27. Klik `Setup Column...`
28. Uncheck kolom `Brand` pada popup Setup Column
29. Geser kolom `Name` satu posisi ke bawah
30. Klik icon Pin pada kolom `Asset ID`
31. Klik `[Reset to Default]`
32. Verifikasi Live Preview kembali ke default modul: visibility, urutan, dan pin
33. Klik `[Save]`
34. Verifikasi tabel memakai konfigurasi default modul setelah `[Save]`
35. Klik header kolom Actions (⋯)
36. Klik `Setup Column...`
37. Uncheck kolom `Brand` pada popup Setup Column
38. Klik ✕ pada popup Setup Column
39. Verifikasi popup tertutup, perubahan dibuang, dan tabel memakai konfigurasi tersimpan terakhir (kolom `Brand` tampil)
40. Klik header kolom Actions (⋯)
41. Klik `Setup Column...`
42. Uncheck kolom `Brand` pada popup Setup Column
43. Tekan Esc
44. Verifikasi popup tertutup, perubahan dibuang, dan tabel memakai konfigurasi tersimpan terakhir (kolom `Brand` tampil)
45. Klik header kolom Actions (⋯)
46. Klik `Setup Column...`
47. Uncheck kolom `Brand` pada popup Setup Column
48. Klik `[Save]`
49. Klik Sub-tab Pending Approvals
50. Verifikasi konfigurasi tabel Sub-tab Pending Approvals tidak berubah: kolom `Transaction ID`, `Transaction`, `Requester`, `Submission Date` tampil dalam urutan default
51. Klik Sub-tab Assigned Assets
52. Verifikasi kolom `Brand` tidak tampil di tabel Sub-tab Assigned Assets (konfigurasi tabel ini tetap tersimpan)
53. Pulihkan konfigurasi kolom tabel Assigned Assets: hapus preferensi kolom di browser
54. Tekan F5 pada halaman Detail
55. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Langkah 3 sampai 16 diulang untuk tiga kelompok tabel parameter "Kelompok Pin" (bagian 8b butir 7); `Verifikasi` memakai "tiap kolom kelompok itu" dan mengasersi setiap kolom kelompok (membeku, bertahan setelah F5, dilepas setelah unpin).
- Langkah pemulihan konfigurasi kolom (23 dan 53) dan F5 sesudahnya memulihkan tabel ke default (S-09); hook `after` mengulang pemulihan sebagai cadangan.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (83 langkah, 55 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Assigned Assets (Setup Column), satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-459 dan 460 ada di spec 156.
- Temuan untuk QA (S-15):
  - TC-FA-SU-461 Expected h ("setelah tiga kolom di-pin ... tooltip") diasersi dengan mem-pin tiga kolom pertama lalu mengarahkan kursor ke icon Pin kolom `Transaction ID` tanpa menyimpan.
  - TC-FA-SU-462 Langkah 2 ("ubah beberapa pengaturan") tidak menyebut pengaturan; spec memakai uncheck `Brand`, geser `Name`, dan pin `Asset ID`. Langkah 6 ("tabel lain yang punya Setup Column") tidak menyebut tabelnya; spec memakai Sub-tab Pending Approvals.
  - Expected a TC-FA-SU-462 ("menjadi permanen hanya setelah [Save]") dapat dibedakan hanya bila konfigurasi sebelum Reset bukan default; spec memulai dari default sehingga yang teramati adalah preview dan tabel kembali default.
