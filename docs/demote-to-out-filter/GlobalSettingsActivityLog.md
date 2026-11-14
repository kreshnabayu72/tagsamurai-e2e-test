# Eliminasi Step: Global Settings > ActivityLog

Modul: ActivityLog, Sumber: specs/GlobalSettings/ActivityLog, Tanggal 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner:** persona aktif dilacak dari Prerequisites dan langkah login, logout, ganti akun, atau ganti company. Langkah yang dijalankan saat persona Distributor atau Partner aktif dikecualikan, termasuk login menuju persona itu. Akun Client (Total Control Client A, B, C, dan seterusnya) bukan Distributor atau Partner, sehingga tidak dikecualikan. Langkah saat persona Principal dipertahankan.
- **B. Halaman detail:** hanya (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya, dan (2) halaman detail client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Global Settings > User, detail user di Fixed Asset > Settings > User, Detail Non-Login User, Detail Role, Detail Brand, dan detail lain tidak termasuk.
- **C. Fitur AI:** tidak ditemukan pada modul ini.
- **D. Menu Approval:** hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- **E. Surface mobile atau Android, serta resize viewport desktop:** langkah yang menguji layout mobile, aplikasi Android, atau bottom sheet mobile. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).
- Langkah login, buka list, dan search yang mendahului halaman detail dipertahankan.

Ringkasan: 6 spek punya eliminasi; 61 dari 2113 langkah bernomor dikecualikan. Langkah yang dikecualikan sebagian (misalnya iterasi persona) dinyatakan di kolom Langkah dikecualikan.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-GS-ACTLOG-E2E-006 | Guided Tooltip: Flag Seen, Replay, dan Keluar Tanpa Selesai | 20-22, 29 (E) | E | resize viewport desktop (langkah 20, 29); verifikasi setelah resize viewport desktop (langkah 21-22) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-ACTLOG-E2E-007 | Mobile: Card Session, Card User Action, Guided Step 2, dan Download | 1-32 (E) | E | Menguji surface mobile atau Android | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-ACTLOG-E2E-011 | Isolasi Entitas: Client, Principal, Distributor, Partner, dan Realtime Lintas Entitas | 44-55 (A) | A | Iterasi baris 4 (Distributor Dua) dan 5 (Partner Tiga): login ke persona Distributor atau Partner (langkah 44) dan langkah yang dijalankan saat persona itu aktif (45-55) | Tidak ada langkah yang dipertahankan bergantung pada langkah 44-55 untuk iterasi Distributor Dua dan Partner Tiga. |
| TC-GS-ACTLOG-E2E-025 | Setup Column Tab Session: Urutan dan Pin Satu Kolom | 12, 15-16, 18-19, 23-25 (E) | E | resize viewport desktop (langkah 12, 25); verifikasi setelah resize viewport desktop (langkah 15-16, 18-19, 23-24) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-ACTLOG-E2E-026 | Setup Column Tab Session: Pin Tiga Kolom, Kolom Ke-4, dan Reset | 2, 7-8, 10-11, 36 (E) | E | resize viewport desktop (langkah 2, 36); verifikasi setelah resize viewport desktop (langkah 7-8, 10-11) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-ACTLOG-E2E-061 | Log Lama Tanpa Batas Waktu untuk Client, Principal, Distributor, Partner | 1-11 (A) | A | Iterasi untuk persona Distributor dan Partner (login entitas dan langkah 2-11 saat persona itu aktif) | Tidak ada langkah yang dipertahankan bergantung pada iterasi Distributor atau Partner; iterasi Client dan Principal tetap berjalan. |

## Ragu / Perlu Konfirmasi

- Spec 011 (A): langkah 44-55 dikecualikan hanya untuk iterasi baris 4 (Distributor Dua) dan 5 (Partner Tiga). Spec menulis satu blok untuk tiga baris tabel, batas iterasi per persona tidak tertulis eksplisit. Konfirmasi granularitas ini.
- Spec 061 (A): langkah 1-11 dijalankan untuk tiap entitas; iterasi Distributor dan Partner dikecualikan, iterasi Client dan Principal dipertahankan. Spec tidak menulis iterasi secara eksplisit. Konfirmasi.
- Spec 007 (E): spec berjalan di browser web dengan viewport mobile (bukan aplikasi). Seluruh langkah diperlakukan sebagai surface mobile dan dikecualikan. Konfirmasi.
