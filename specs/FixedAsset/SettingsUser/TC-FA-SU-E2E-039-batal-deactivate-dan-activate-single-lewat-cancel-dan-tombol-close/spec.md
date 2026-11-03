---
id: TC-FA-SU-E2E-039-batal-deactivate-dan-activate-single-lewat-cancel-dan-tombol-close
title: "Batal Deactivate dan Activate Single lewat Cancel dan Tombol Close: Sakelar Kembali Tanpa Perubahan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-89
  - TC-FA-SU-90
coverage:
  web: automated
---

# Batal Deactivate dan Activate Single lewat Cancel dan Tombol Close: Sakelar Kembali Tanpa Perubahan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`. Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Client `FaUserMain` (#20). Spec memakai pengguna milik spec (S-06).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE):
  - `Gita Permata {runId}-039`, email `gita.permata+{runId}-039@qwertysystem.net`: Active (TC-FA-SU-89).
  - `Doni Prasetyo {runId}-039`, email `doni.prasetyo+{runId}-039@qwertysystem.net`: Inactive (TC-FA-SU-90).
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): hook `before` mencatat baseline jumlah entri kedua pengguna pada Tab Changelog target serta total entri Tab System Log aktor dan Activity Log; asersi "tidak ada entri baru" berupa jumlah sama dengan baseline, bukan angka absolut (S-12).
- Kemampuan teknis: pencatat request jaringan Spectra untuk memastikan tidak ada request simpan status yang terkirim.
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-89: Batalkan Deactivate lewat `[Cancel]` dan `[×]`

1. Ketik Search `Gita Permata {runId}-039`, tekan Enter
2. Klik sakelar Active pada baris `Gita Permata {runId}-039`
3. Klik `[Cancel]`
4. Verifikasi dialog `Deactivate User` tertutup
5. Verifikasi sakelar Active baris `Gita Permata {runId}-039` kembali ke ON
6. Klik sakelar Active pada baris `Gita Permata {runId}-039`
7. Klik `[×]` pada dialog
8. Verifikasi dialog `Deactivate User` tertutup
9. Verifikasi sakelar Active baris `Gita Permata {runId}-039` kembali ke ON
10. Verifikasi tidak ada request simpan status yang terkirim sejak langkah 2
11. Verifikasi tidak ada toast
12. Verifikasi jumlah entri Tab Changelog `Gita Permata {runId}-039`, total entri Tab System Log aktor, dan total entri Activity Log sama dengan baseline

### TC-FA-SU-90: Batalkan Activate lewat `[Cancel]` dan `[×]`

13. Ganti isi kotak search dengan `Doni Prasetyo {runId}-039`, tekan Enter
14. Klik sakelar Active pada baris `Doni Prasetyo {runId}-039`
15. Klik `[Cancel]`
16. Verifikasi dialog `Activate User` tertutup
17. Verifikasi sakelar Active baris `Doni Prasetyo {runId}-039` kembali ke OFF
18. Klik sakelar Active pada baris `Doni Prasetyo {runId}-039`
19. Klik `[×]` pada dialog
20. Verifikasi dialog `Activate User` tertutup
21. Verifikasi sakelar Active baris `Doni Prasetyo {runId}-039` kembali ke OFF
22. Verifikasi tidak ada toast
23. Verifikasi jumlah entri Tab Changelog `Doni Prasetyo {runId}-039`, total entri Tab System Log aktor, dan total entri Activity Log sama dengan baseline

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16) dan langkah 13 (mengganti isi kotak search yang masih berisi `Gita Permata {runId}-039`, bagian 8b butir 9).
- Pembagian TC lintas spec: TC-FA-SU-87 dan TC-FA-SU-88 (konfirmasi Deactivate dan Activate dengan asersi log) ada di spec 029. Klausa "tanpa entri log" TC-FA-SU-89 dan TC-FA-SU-90 diasersi sebagai jumlah terhadap baseline di spec ini (aksi pembatalan, bukan spec absence); anchor-nya jumlah awal yang dicatat hook `before`.
- Dialog yang dibuka pada langkah 2, 6, 14, dan 18 tidak diasersi terbuka karena Expected TC hanya menyatakan hasil penutupan.
- Temuan untuk QA:
  - Post Condition TC-FA-SU-89 dan TC-FA-SU-90 ("tidak ada entri baru pada tiga permukaan log") sama dengan klausa Expected butir c dan diasersi pada langkah 12 dan 23. TC tidak menyebut jalur navigasi ketiga surface log; asersi memakai kemampuan baca log.
  - Tab Changelog pengguna hasil seed dapat kosong (baseline nol); asersi berupa jumlah sama dengan baseline, bukan asersi absence.
  - Target TC (Gita Permata, Doni Prasetyo) adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec bernama sama dengan suffix (S-06).
