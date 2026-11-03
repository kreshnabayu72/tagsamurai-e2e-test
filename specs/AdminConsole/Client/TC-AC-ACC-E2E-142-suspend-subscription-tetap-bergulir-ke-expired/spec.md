---
id: TC-AC-ACC-E2E-142-suspend-subscription-tetap-bergulir-ke-expired
title: "Subscription Tetap Bergulir ke Expired Selama Client Suspended (Job Scheduler Lifecycle dan Pengaturan Jam)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-195
coverage:
  web: automated
---

# Subscription Tetap Bergulir ke Expired Selama Client Suspended (Job Scheduler Lifecycle dan Pengaturan Jam)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data (Tabel A3, kelas Dikonsumsi): C-ISO-7 `PT Suspend Hampir Habis` (Active; FAMS satu-satunya term Active dengan End = tanggal seed + 7 hari, tampil di Tab Subscription sub-tab FAMS > Subscription Details). Fixture BE (disediakan tim FE/BE, idempotent) men-seed ulang C-ISO-7 di hook `before` dan `after` (term sudah Expired dan Client Suspended setelah spec ini berjalan).
- Konfigurasi tenant uji: durasi status Expired pada Lifecycle Settings lebih panjang dari satu hari (nilai dimiliki Lifecycle Settings dan tidak diasersi modul Client).
- Kemampuan teknis (kelas d: background job dan waktu): mengatur jam server dan jam browser secara absolut ke pukul 01:00 pada hari setelah End term (E) dalam zona waktu General Settings (bukan digeser relatif; jam browser ikut diatur karena sel badge diamati lewat UI); memicu atau menunggu satu siklus job scheduler lifecycle dengan polling (muat ulang sub-tab Suspended tiap 5 detik, batas tunggu 2 menit). Jam dipulihkan ke waktu nyata di akhir spec dan di hook `after` (S-09).
- Kemampuan teknis (sesi): sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser).
- State global: jam server dan jam browser; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-195: Subscription tetap bergulir ke Expired selama Client Suspended

1. Ketik Search `PT Suspend Hampir Habis`, tekan Enter
2. Klik Company Name `PT Suspend Hampir Habis`, buka Tab Subscription sub-tab FAMS, dan catat End pada Subscription Details sebagai E
3. Verifikasi Status badge FAMS `Active`
4. Verifikasi End terisi tanggal (E)
5. Klik breadcrumb "Client"
6. Ketik Search `PT Suspend Hampir Habis`, tekan Enter
7. Klik `[⋯]` pada baris `PT Suspend Hampir Habis` → pilih `Suspend`, lalu klik `[Suspend]` pada dialog
8. Klik sub-tab Suspended, ketik Search `PT Suspend Hampir Habis`, tekan Enter
9. Lihat sel FAMS baris `PT Suspend Hampir Habis`
10. Verifikasi baris `PT Suspend Hampir Habis` tampil di sub-tab Suspended
11. Verifikasi sel FAMS `Active`
12. Atur jam server dan jam browser ke pukul 01:00 pada hari setelah E (zona waktu General Settings)
13. Polling antrean job scheduler lifecycle: muat ulang sub-tab Suspended tiap 5 detik sampai satu siklus job selesai (batas tunggu 2 menit)
14. Ketik Search `PT Suspend Hampir Habis`, tekan Enter dan lihat sel FAMS baris `PT Suspend Hampir Habis`
15. Verifikasi sel FAMS `Expired` (dampak transisi lifecycle pada badge)
16. Verifikasi baris `PT Suspend Hampir Habis` tetap berada di sub-tab Suspended (transisi lifecycle tidak diblok flag Suspend)
17. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 5 (kembali ke List), langkah 7 (Suspend yang merupakan langkah TC 4), dan langkah 17 (pemulihan jam; Post Condition TC-AC-ACC-195 butir a). Post Condition butir b (seed ulang C-ISO-7) dijalankan di hook.
- Jam diatur absolut ke End (E) + 1 hari pukul 01:00 (konvensi bagian 6), bukan digeser relatif; E dibaca dari Subscription Details di UI sesuai TC.
- Temuan untuk QA:
  - TC-AC-ACC-195 langkah 6 ("tunggu satu siklus job scheduler lifecycle") tidak menyebut interval atau cara memicu job; spec memakai polling dengan batas tunggu 2 menit (idiom bagian 6) dan kemampuan pemicu job disediakan tim FE/BE.
  - TC-AC-ACC-195 berlabel "Manual Only: menunggu job scheduler"; kebutuhan pengaturan jam dan job dicatat di Prerequisites.
