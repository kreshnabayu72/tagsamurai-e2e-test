---
id: TC-FA-SU-E2E-168-sub-tab-pending-approvals-pin-dan-unpin-setup-column
title: "Sub-tab Pending Approvals: Pin dan Unpin Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-492
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Pin dan Unpin Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#25): Detail Budi Santoso dengan Sub-tab Pending Approvals 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #25 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC:

| Transaction ID | Transaction | Requester | Submission Date |
|---|---|---|---|
| `BRW-20260712-0341` | `Borrow` | `Ahmad D` | 12/07/26 |
| `TRF-20260714-0088` | `Transfer` | `Citra L` (Citra Lestari) | 14/07/26 |
| `DSP-20260715-0022` | `Disposal` | `Eka W` | 15/07/26 |
| `ASG-20260716-0015` | `Assignment` | `Budi S` | 16/07/26 |
| `BRW-20260718-0007` | `Borrow` | `Citra L` (Citra Lestari) | 18/07/26 |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).
- Tabel parameter "Kelompok Pin" (dipakai langkah 3 sampai 16):

| Kelompok | Kolom |
|---|---|
| 1 | `Transaction ID`, `Transaction`, `Requester` |
| 2 | `Submission Date` |

Maksimum tiga kolom di-pin sekaligus, sehingga kolom di-pin per kelompok dan di-unpin sebelum kelompok berikutnya.
- Kemampuan menghapus preferensi kolom Setup Column di browser (disediakan tim FE): dipakai sebagai langkah pemulihan dan di hook `after` untuk tabel yang konfigurasinya disimpan spec ini (bagian 4 konvensi). Konfigurasi kolom tersimpan per perangkat dan per tabel.
- Kemampuan teknis: viewport browser dipersempit agar tabel dapat di-scroll horizontal (disediakan tim FE).

## Test Steps

### TC-FA-SU-492: Pin dan unpin Setup Column Sub-tab Pending Approvals kelas Hideable (default tampil)

1. Ketik Search `Budi Santoso`, tekan Enter, lalu klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
3. Untuk setiap baris tabel parameter "Kelompok Pin" (langkah 3 sampai 16): klik header kolom Actions (⋯)
4. Klik `Setup Column...`
5. Klik icon Pin pada tiap kolom kelompok itu
6. Klik `[Save]`
7. Scroll tabel secara horizontal
8. Verifikasi tiap kolom kelompok itu membeku di kiri saat tabel di-scroll horizontal
9. Tekan F5 pada halaman Detail
10. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
11. Verifikasi tiap kolom kelompok itu tetap membeku di kiri setelah F5
12. Klik header kolom Actions (⋯)
13. Klik `Setup Column...`
14. Klik icon Pin yang aktif pada tiap kolom kelompok itu untuk unpin
15. Klik `[Save]`
16. Verifikasi tiap kolom kelompok itu tidak lagi membeku saat tabel di-scroll horizontal
17. Klik header kolom Actions (⋯)
18. Klik `Setup Column...`
19. Klik icon Pin pada kolom `Transaction ID`, `Transaction`, dan `Requester`
20. Hover icon Pin kolom `Submission Date`
21. Verifikasi icon Pin kolom `Submission Date` disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
22. Klik ✕ pada popup Setup Column untuk membuang perubahan
23. Pulihkan konfigurasi kolom tabel Pending Approvals: hapus preferensi kolom di browser
24. Tekan F5 pada halaman Detail
25. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): Search nama `Budi Santoso` serta pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Langkah 3 sampai 16 diulang untuk dua baris tabel parameter "Kelompok Pin" (bagian 8b butir 7); `Verifikasi` memakai "tiap kolom kelompok itu" dan mengasersi setiap kolom kelompok.
- Langkah pemulihan konfigurasi kolom (23) dan F5 sesudahnya memulihkan tabel ke default (S-09); hook `after` mengulang pemulihan sebagai cadangan.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (39 langkah, 25 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Pending Approvals (Pin), satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-491 dan 493 ada di spec 165.
- Temuan untuk QA (S-15):
  - TC-FA-SU-492 Expected e ("setelah tiga kolom di-pin ... tooltip") diasersi dengan mem-pin tiga kolom pertama lalu mengarahkan kursor ke icon Pin kolom `Submission Date` tanpa menyimpan.
