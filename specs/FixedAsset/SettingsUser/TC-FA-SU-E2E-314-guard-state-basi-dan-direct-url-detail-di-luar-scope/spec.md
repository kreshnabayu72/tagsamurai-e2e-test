---
id: TC-FA-SU-E2E-314-guard-state-basi-dan-direct-url-detail-di-luar-scope
title: "Guard State Basi dan Direct URL Detail di Luar Scope"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1005
  - TC-FA-SU-1006
  - TC-FA-SU-1007
coverage:
  web: automated
---

# Guard State Basi dan Direct URL Detail di Luar Scope

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 9 Manage global user & role (Update) Qori Akbar (Pre-setup #4; email disediakan tim FE; `Spectra.env.FA_MURG_UPD_PASSWORD`); langkah 21 Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; email disediakan tim FE; `Spectra.env.FA_MURGR_UPD_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Admin B (#13), dan Global Settings (#38). Target baca langkah 22-26: Indra Wijaya Pre-setup (di luar scope Finance & Accounting; tidak diubah spec ini).
- Pengguna milik spec (target aksi tulis; dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan; disediakan tim FE):
  - `Rudi Hartono {runId}-314`, email `rudi.hartono+{runId}-314@qwertysystem.net`: Active; aktif di Global Settings (sakelar FAMS ON); di luar scope Finance & Accounting (target TC-FA-SU-1006).
  - `Gita Permata {runId}-314`, email `gita.permata+{runId}-314@qwertysystem.net`: Active; bukan Total Control; di luar scope Finance & Accounting (target TC-FA-SU-1005).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Sesi API Admin B (Total Control, Pre-setup #13) dan Principal Automation (Pre-setup #12) untuk memicu perubahan state lewat sesi API (langkah 11 dan 2), disediakan tim FE/BE; sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi (P-2 tidak berlaku).
- Rudi Hartono milik spec dibuat aktif di Global Settings oleh seed API di hook `before` sehingga langkah 2 membentuk tampilan basi (lihat Temuan untuk QA); pengguna Pre-setup #38 tidak disentuh.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum aksi (baseline, S-12) dan sesudah aksi; audit trail permanen sehingga asersi memakai selisih terhadap baseline. Log yang eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- Pencatat request jaringan halaman untuk langkah 22 dan pola URL Detail pengguna disediakan tim FE/BE (tidak tertulis di TC).
- State global dan pemulihan: tidak ada; perubahan hanya pada Gita Permata dan Rudi Hartono milik spec yang dihapus di hook `after`. Efek pada Pre-setup: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1006: Guard saat target nonaktif di Global Settings pada tampilan basi

1. Ketik Search `Rudi Hartono {runId}-314`, tekan Enter sehingga baris Rudi Hartono {runId}-314 tampil dengan sakelar Active Enabled (tampilan sesi A)
2. Principal Automation menonaktifkan Rudi Hartono {runId}-314 di Global Settings lewat sesi API hingga status nonaktif tersimpan (tanpa memuat ulang User List)
3. Klik sakelar Active baris Rudi Hartono {runId}-314 pada tampilan basi
4. Klik `[Deactivate]` pada dialog konfirmasi
5. Verifikasi toast error "This user is inactive in Global Settings. Contact a Global Settings admin to reactivate."
6. Verifikasi sakelar Active baris Rudi Hartono {runId}-314 dikembalikan ke posisi semula (ON)
7. Muat ulang User List, lalu ganti isi kotak search dengan `Rudi Hartono {runId}-314`, tekan Enter
8. Verifikasi sakelar Active baris Rudi Hartono {runId}-314 berubah ke state Disabled setelah User List di-refresh

### TC-FA-SU-1005: Guard dievaluasi ulang saat state berubah di antara render dan klik

9. Ganti akun: logout, login sebagai Qori Akbar (Manage global user & role (Update), `Spectra.env.FA_MURG_UPD_PASSWORD`), buka Fixed Asset > Settings > User, lalu Ketik Search `Gita Permata {runId}-314`, tekan Enter; klien HTTP memakai token sesi API akun yang sama
10. Catat jumlah entri log pada Tab Changelog Gita Permata {runId}-314, Tab System Log aktor, dan Activity Log sebagai baseline
11. Admin B (Total Control, sesi API) menetapkan Gita Permata {runId}-314 sebagai Total Control lewat Role & Permission hingga penetapan tersimpan (tanpa memuat ulang User List sesi A)
12. Klik sakelar Active baris Gita Permata {runId}-314 pada tampilan basi
13. Klik `[Deactivate]` pada dialog konfirmasi
14. Verifikasi toast error "You don't have permission to edit."
15. Verifikasi sakelar Active baris Gita Permata {runId}-314 dikembalikan ke nilai server (ON)
16. Muat ulang halaman User List, lalu ganti isi kotak search dengan `Gita Permata {runId}-314`, tekan Enter
17. Hover sakelar Active baris Gita Permata {runId}-314
18. Verifikasi sakelar Active baris Gita Permata {runId}-314 Disabled dengan tooltip "You don't have permission to edit."
19. Verifikasi status Gita Permata {runId}-314 tidak berubah (tetap Active)
20. Verifikasi jumlah entri log pada Tab Changelog Gita Permata {runId}-314, Tab System Log aktor, dan Activity Log sama dengan baseline

### TC-FA-SU-1007: Akses Detail langsung via URL di luar scope

21. Ganti akun: logout, login sebagai Sinta Dewi (Manage user & role Group (Update), `Spectra.env.FA_MURGR_UPD_PASSWORD`), lalu buka Fixed Asset > Settings > User; klien HTTP memakai token sesi API akun yang sama
22. Aktifkan pencatat request jaringan halaman, lalu buka URL Detail Indra Wijaya langsung
23. Verifikasi toast error "You don't have permission to do this." tampil
24. Verifikasi header dan tab Detail tidak dirender dan area konten kosong
25. Verifikasi halaman tidak dialihkan (URL tetap URL Detail Indra Wijaya)
26. Verifikasi respons jaringan tidak memuat data pengguna Indra Wijaya

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah (TC-FA-SU-1006, 1005, 1007) supaya ganti akun hanya dua kali dan aktor default suite menjalankan blok pertama.
- TC-FA-SU-1005 dan 1006 berlabel `Manual Only (d) dua sesi paralel`; pelaku kedua (Admin B dan Principal) memakai sesi API (R-20) sehingga TC tetap masuk spec ini tanpa butir `P-2`.
- TC-FA-SU-1005 Expected c (tidak ada perubahan data dan tidak ada entri log) adalah asersi jumlah dengan baseline (S-12), bukan asersi absence kelas g. Post Condition TC-FA-SU-1006 "tidak ada entri baru pada tiga permukaan log" tidak punya langkah observasi dan tidak diasersi (S-01, S-05).
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 7, 10, 16. Langkah 1, 7, 9, dan 16 juga Search untuk menemukan baris target milik spec (R-16); langkah 7 dan 16 memuat ulang User List sehingga pencarian diulang.
- Ganti akun eksplisit (S-07): langkah 9, 21.
- Asersi toast (langkah 23) diletakkan sebelum asersi konten Detail kosong (langkah 24) karena toast bersifat sementara (8b.5, 8b.11).
- Temuan untuk QA:
  - Pre-setup #38 menyebut Rudi Hartono sudah nonaktif di Global Settings, sedangkan Langkah Uji 2 TC-FA-SU-1006 menonaktifkannya; spec memakai Rudi milik spec yang dibuat aktif lewat seed API.
  - Cara Admin B menetapkan Gita sebagai Total Control "lewat Role & Permission" tidak dirinci TC; dilakukan lewat sesi API (disediakan tim FE/BE).
  - TC-FA-SU-1005 tidak menyebut dialog konfirmasi secara eksplisit selain `[Deactivate]`; spec mengikuti Langkah Uji.
  - Email dan password Qori Akbar (#4) dan Sinta Dewi (#6) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
