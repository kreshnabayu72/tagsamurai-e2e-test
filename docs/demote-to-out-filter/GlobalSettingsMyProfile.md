# Eliminasi Step: Global Settings > MyProfile

Modul: MyProfile  
Sumber: specs/GlobalSettings/MyProfile  
Tanggal: 2026-11-14

## Kriteria

- A. Persona Distributor atau Partner: langkah yang dijalankan saat persona Distributor atau Partner aktif (termasuk login menuju persona itu). Persona Principal tetap dipertahankan.
- B. Halaman detail: (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya; (2) halaman detail client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Tidak termasuk B: detail user di Global Settings > User, detail user di Fixed Asset > Settings > User, Detail Login User yang dibuka dari Global Settings, Detail Non-Login User, Detail Role, Detail Brand, dan detail lain.
- C. Fitur AI (modul Import): langkah yang menguji AI, termasuk setup mock AI yang hanya untuk AI.
- D. Menu Approval: hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- E. Surface mobile atau Android, serta resize viewport desktop. Yang dikecualikan: langkah yang mengubah atau memulihkan ukuran viewport browser desktop, dan langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize). Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan.
- Catatan modul: Tidak ada persona Distributor atau Partner di modul ini.
- Langkah login, buka list, dan search yang mendahului halaman detail dipertahankan. Yang dikecualikan hanya langkah yang membuka atau berada di halaman detail (keputusan user 2026-11-14).

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-GS-PROFILE-E2E-007-guided-tooltip-interupsi-dan-keyboard | Guided Tooltip: resize viewport, navigasi keluar, dan operasi keyboard | 4-8 (E) | E | resize viewport desktop (langkah 4, 6); verifikasi setelah resize viewport desktop (langkah 5, 7-8) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-PROFILE-E2E-009-tampilan-mobile-android | Mobile Android: card satu kolom, bottom sheet Avatar, bottom sheet Change Password, dan Guided Tooltip mobile | 1-23, 25-26 | E | Seluruh langkah dijalankan di aplikasi Android (surface mobile): card, bottom sheet, Tap, login ulang di app Android | Tidak ada langkah non-E yang bergantung pada state spec ini |
| TC-GS-PROFILE-E2E-055-sinkron-foto-lintas-modul | Sinkron Foto: Fixed Asset, Admin Console, Recycle Bin, dan Changelog File Manager | 6-8 | B | Membuka Detail Andi Pratama di Admin Console > Settings > User (langkah 6) dan memverifikasi Avatar Header Detail user di Admin Console (7-8); langkah 3-5 (buka list dan search) tetap dipertahankan | Tidak ada |
| TC-GS-PROFILE-E2E-065-biometric-dicabut-setelah-change-password | Change Password Mencabut Kredensial Biometric Lintas Device | 4-6 | E | Langkah pada perangkat Android (login ulang biometric di aplikasi mobile) | Tidak ada |

## Ragu / Perlu Konfirmasi

- 009 langkah 25 tercatat dua kali di Test Steps (Tap [Next]); nomor dicatat apa adanya.
- 065 langkah 6 tidak menyebut perangkat secara eksplisit; dikecualikan mengikuti langkah 4-5 (Android).
