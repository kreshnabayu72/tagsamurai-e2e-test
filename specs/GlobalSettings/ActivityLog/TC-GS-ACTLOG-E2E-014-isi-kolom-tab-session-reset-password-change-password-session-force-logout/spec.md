---
id: TC-GS-ACTLOG-E2E-014-isi-kolom-tab-session-reset-password-change-password-session-force-logout
title: "Isi Kolom Tab Session: Reset Password, Change Password, Session, Force-Logout"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-44
  - TC-GS-ACTLOG-45
  - TC-GS-ACTLOG-46
  - TC-GS-ACTLOG-48
  - TC-GS-ACTLOG-226
coverage:
  web: automated
---

# Isi Kolom Tab Session: Reset Password, Change Password, Session, Force-Logout

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun entitas tanpa Concurrent (`Fixture.activityLog.entitasTanpaConcurrent`) dan halaman Portal serta Global Settings > Activity Log (kemampuan disediakan tim FE/BE).
- Akun yang diuji (spec berganti akun secara eksplisit di akhir):

  | Urutan | TC | Role | Email | Env var password |
  |---|---|---|---|---|
  | 1 | TC-GS-ACTLOG-44, 45, 46, 48 | Total Control Client A (Sari Dewi) | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
  | 2 | TC-GS-ACTLOG-226 | Total Control entitas uji tanpa lisensi Concurrent produk apa pun | `Fixture.activityLog.entitasTanpaConcurrent` (disediakan tim FE; email ditetapkan tim FE) | `Spectra.env.GS_NOCONCURRENT_TC_PASSWORD` (env baru) |

  Login akun 1 di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun 1, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD`, `GS_NOCONCURRENT_TC_PASSWORD`, `ACTLOG_PASSWORD` (password uji user dinamis), `ACTLOG_PASSWORD_NEW` (password baru hasil Change Password); password salah memakai `LP_PASSWORD_WRONG`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat API di hook `before`:
  - `Siti Nurbaya {runId}-014`: Reset Password `Success` (Note `Password reset requested`) dari IP `2001:db8::1a` dengan Device `Safari on iOS`.
  - `Budi Anwar {runId}-014`: Reset Password `Failed` (Note `Too many reset attempts`); Change Password `Success` (Note `Password changed`) dan Change Password `Failed` (Note `Incorrect current password`) hasil alur Change Password modul My Profile.
  - `John Doe {runId}-014` dengan akses Fixed Asset: Login platform, lalu sesi platformnya diakhiri oleh Admin Force-Logout lewat License > Concurrent produk Fixed Asset (cascade); entri Login platform ada.
  - Password semua user di atas `Spectra.env.ACTLOG_PASSWORD`.
- Kemampuan teknis (disediakan tim FE/BE): (a) alamat sumber request dan User-Agent Reset Password dapat diatur (`2001:db8::1a`, `Safari on iOS`); (b) pemicu `Too many reset attempts` lewat alur Reset Password Auth; (c) Admin Force-Logout atas `John Doe {runId}-014` lewat License > Concurrent Fixed Asset oleh admin pemegang akses itu (akun dan endpoint tidak ditentukan di TC); (d) buka dan tutup card Global Settings dari Portal (UI, atau API Auth) untuk TC-GS-ACTLOG-46 dan TC-GS-ACTLOG-226.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua user bersuffix `{runId}-014`.
- Spec tidak mengubah jam.

## Test Steps

### TC-GS-ACTLOG-44: Baris Reset Password Success dan Failed

1. Buka Global Settings > Activity Log > Session
2. Ketik Search `Siti Nurbaya {runId}-014`, tekan Enter
3. Verifikasi baris Reset Password milik `Siti Nurbaya {runId}-014`: Activity `Reset Password`, Status `Success`, Note `Password reset requested`, IP Address `2001:db8::1a`, Device / Browser `Safari on iOS`
4. Ganti isi kotak search dengan `Budi Anwar {runId}-014`, tekan Enter
5. Verifikasi baris Reset Password milik `Budi Anwar {runId}-014`: Activity `Reset Password`, Status `Failed`, Note `Too many reset attempts`

### TC-GS-ACTLOG-45: Baris Change Password Success dan Failed

6. Verifikasi baris Change Password milik `Budi Anwar {runId}-014` yang Success: Activity `Change Password`, Status `Success`, Note `Password changed`
7. Verifikasi baris Change Password milik `Budi Anwar {runId}-014` yang Failed: Activity `Change Password`, Status `Failed`, Note `Incorrect current password`

### TC-GS-ACTLOG-46: Event buka dan tutup Global Settings sebagai produk tampil sebagai Activity Session

8. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel, ketik Search `Sari Dewi`, tekan Enter, klik icon Filter, pilih Activity `Session`, klik [Apply], lalu catat jumlah baris `Session started` dan jumlah baris `Session ended` milik user penguji sebagai baseline
9. Buka Portal, klik card Global Settings
10. Buka Global Settings > Activity Log > Session, ketik Search `Sari Dewi`, tekan Enter
11. Verifikasi jumlah baris `Session started` milik user penguji bertambah tepat satu dibanding baseline langkah 8, dengan Activity `Session`, Status `—`, Note `Session started`
12. Tutup card Global Settings (akhiri sesi produk)
13. Muat ulang tab Session, lalu ketik Search `Sari Dewi`, tekan Enter, klik icon Filter, pilih Activity `Session`, klik [Apply]
14. Verifikasi jumlah baris `Session ended` milik user penguji bertambah tepat satu dibanding baseline langkah 8, dengan Activity `Session`, Status `—`, Note `Session ended`

### TC-GS-ACTLOG-48: Admin Force-Logout tercatat sebagai baris Logout dengan Note Logged out by admin

15. Buka Portal, klik card Global Settings, buka Global Settings > Activity Log > Session
16. Ketik Search `John Doe {runId}-014`, tekan Enter
17. Klik icon Filter, pilih Activity `Logout`, klik [Apply]
18. Verifikasi satu baris Activity `Logout`, Status `—`, Note `Logged out by admin`, User `John D` tampil
19. Klik [Clear Field], pilih Activity `Session`, klik [Apply]
20. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
21. Verifikasi baris Activity `Session` dengan Note `Session started` milik user penguji tampil
22. Ketik Search `Logged out by admin`, tekan Enter
23. Verifikasi tidak ada baris Activity `Session` dengan Note `Logged out by admin`
24. Klik icon Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-GS-ACTLOG-226: Tab Session menampilkan baris sesi Global Settings untuk entitas tanpa lisensi produk

25. Logout, lalu login sebagai Total Control entitas tanpa lisensi Concurrent dengan `Spectra.env.GS_NOCONCURRENT_TC_PASSWORD`
26. Buka Portal, klik card Global Settings
27. Tutup card Global Settings (akhiri sesi produk)
28. Buka Portal, klik card Global Settings, lalu buka Global Settings > Activity Log > Session
29. Klik icon Filter, pilih Activity `Session`, klik [Apply]
30. Verifikasi hanya Note `Session started` dan `Session ended` yang tampil pada kolom Note
31. Verifikasi tidak ada Note `Concurrent limit reached` pada kolom Note

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-44, 45, 46, 48, 226).
- Langkah penghubung (tanpa awalan `Verifikasi`): mengetik atau mengganti Search nama subjek bersuffix (langkah 2, 4, 10, 16, 22) agar baris subjek ditemukan di antara baris run lain; pemulihan state antar TC (langkah 8, 20, 24: menutup Search lewat `(←)` dan mengosongkan Filter; langkah 8 dan 13 juga menerapkan ulang Search dan Filter karena state keduanya setelah muat ulang atau pindah halaman tidak ditetapkan PRD); membuka Portal dan card Global Settings setelah sesi produk ditutup (langkah 15 dan 28); langkah 25 ganti akun. Langkah 6 dan 7 memakai hasil Search `Budi Anwar {runId}-014` dari langkah 4 tanpa Search ulang.
- TC-GS-ACTLOG-46: Expected a dan b memakai baseline jumlah baris sebelum dan sesudah aksi (S-12) pada hasil Search `Sari Dewi` dengan filter Activity `Session`, bukan posisi "teratas" dan bukan penanda waktu. Dependensi TC-GS-ACTLOG-226 pada TC-GS-ACTLOG-46 disalin utuh sebagai langkah 26 dan 27 (buka lalu tutup card Global Settings) di akun entitas tanpa lisensi.
- TC-GS-ACTLOG-48: Expected b ("Tidak ada baris Activity `Session` dengan Note `Logged out by admin`") dilakukan pada hasil filter Activity `Session` dengan anchor positif langkah 21 (baris Session milik user penguji dari TC-GS-ACTLOG-46 tampil) dan Search `Logged out by admin` (langkah 22) yang ditambahkan sebagai cara mengamati kolom Note; langkah 20 menutup Search sebelum langkah 21 supaya anchor dinilai pada tabel yang sudah direset. Ini asersi pada hasil filter, bukan spec absence kelas g; baris `Logged out by admin` itu sendiri dijadikan asersi presence pada langkah 18. Tidak ada spec absence untuk TC-GS-ACTLOG-48 di slice ini.
- TC-GS-ACTLOG-47 (Concurrent limit reached tidak muncul) ada di spec `TC-GS-ACTLOG-E2E-015-absence-concurrent-limit-download-dan-aksi-sumber-gagal-tidak-tercatat`.
- Temuan untuk QA:
  - TC-GS-ACTLOG-48 menyatakan baris `Logged out by admin` tampil di Tab Session (mengikuti Expected TC dan NC-10), sedangkan Coverage Ledger baris `ACTLOG-LOGIC-02c: Logged out by admin tidak pernah muncul` memetakan TC-GS-ACTLOG-48 sebagai "tidak pernah muncul". Spec mengikuti Expected TC.
  - TC-GS-ACTLOG-48 tidak menyebut admin dan endpoint Force-Logout lewat License > Concurrent; kemampuan itu ditulis sebagai disediakan tim FE/BE.
  - TC-GS-ACTLOG-226 menyebut "entitas uji tanpa lisensi Concurrent" tanpa akun; akun disediakan tim FE (email dan env `GS_NOCONCURRENT_TC_PASSWORD` ditetapkan tim FE, env baru).
  - TC-GS-ACTLOG-46 tidak menyebut cara membuka Portal setelah card ditutup; spec membuka Portal lalu card Global Settings pada langkah 15 dan 28.
  - TC-GS-ACTLOG-46 langkah 3 dan 4 ("Tutup card Global Settings", lalu "Muat ulang tab Session") tidak menyebut layar tempat muat ulang dilakukan dan apakah muat ulang membuka sesi baru (`Session started` tambahan); spec mengikuti TC apa adanya (langkah 12 dan 13).
  - Nama env baru `ACTLOG_PASSWORD_NEW` dan `GS_NOCONCURRENT_TC_PASSWORD` perlu didaftarkan tim FE.
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 17 mengikuti TC-GS-ACTLOG-48 dan pada langkah 29 mengikuti TC-GS-ACTLOG-226; langkah 8, 13, dan 24 adalah langkah penghubung yang bergantung pada perilaku itu.
