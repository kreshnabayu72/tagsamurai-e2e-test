# Eliminasi Step: Global Settings > HardwareHandheldReader

Modul: HardwareHandheldReader, Sumber: specs/GlobalSettings/HardwareHandheldReader, Tanggal 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner:** persona aktif dilacak dari Prerequisites dan langkah login, logout, ganti akun, atau ganti company. Langkah yang dijalankan saat persona Distributor atau Partner aktif dikecualikan, termasuk login menuju persona itu. Akun Client (Total Control Client A, B, C, dan seterusnya) bukan Distributor atau Partner, sehingga tidak dikecualikan. Langkah saat persona Principal dipertahankan.
- **B. Halaman detail:** hanya (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya, dan (2) halaman detail client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Global Settings > User, detail user di Fixed Asset > Settings > User, Detail Non-Login User, Detail Role, Detail Brand, dan detail lain tidak termasuk.
- **C. Fitur AI:** tidak ditemukan pada modul ini.
- **D. Menu Approval:** hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Langkah yang dikecualikan sebagai D di modul ini: TC-GS-HHR-E2E-069 langkah 11, 53, 79, 84-89. Approve atau Reject lewat sesi API di luar menu Admin Console > Approvals tidak dikecualikan.
- **E. Surface mobile atau Android, serta resize viewport desktop:** langkah yang menguji layout mobile, aplikasi Android, atau bottom sheet mobile. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).
- Langkah login, buka list, dan search yang mendahului halaman detail dipertahankan.

Ringkasan: 4 spek punya eliminasi; 80 dari 4987 langkah bernomor dikecualikan. Langkah yang dikecualikan sebagian (misalnya iterasi persona) dinyatakan di kolom Langkah dikecualikan.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-GS-HHR-E2E-006 | Guided Tooltip Halaman Handheld Reader: Muncul Otomatis, Done, Skip, Klik Overlay Menandai Seen, Replay lewat [?], serta Resize dan Navigasi Keluar Tidak Menandai Seen | 35-38, 44 (E) | E | resize viewport desktop (langkah 35, 44); verifikasi setelah resize viewport desktop (langkah 36-38) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-HHR-E2E-014 | Pintu Masuk Activate Reader: Overlay Select Range Type, Penutupan Overlay, Popup Menunggu Sync, dan Resolusi Minimum 1280x720 | 39, 49 (E) | E | resize viewport desktop | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-HHR-E2E-069 | Keputusan Approval Principal atas Collision: Approve, Reject, Cancel Request, Pencatatan Log, dan Isolasi Tenant Lain | 11, 53, 79, 84-89 (D) | D | Masuk atau beroperasi di Admin Console > Approvals (menu Approval belum dibuat) | Langkah 11 dan 53 (Approve dan Reject di Approvals) dikecualikan, sehingga langkah 15, 27, 34, 61, 63, 70, 93 yang memverifikasi hasil keputusan kehilangan pemicunya di spec ini; perlu ditinjau. Langkah 3, 46, 78 (pemulihan fixture) tetap dipertahankan. |
| TC-GS-HHR-E2E-076 | Mobile (Viewport di Bawah 768px): Layout Card List, Toolbar Ikon, Selection Mode, Bottom Sheet, dan Activate Reader Disembunyikan | 1-67 (E) | E | Menguji surface mobile atau Android | Tidak ada ketergantungan yang terdeteksi. |

## Ragu / Perlu Konfirmasi

- Spec 069 langkah 9, 32-34, 50, 71-73: buka System Log di Admin Console untuk akun Principal. Tidak menyebut halaman detail user di Admin Console > Settings > User List, sehingga dipertahankan. Konfirmasi apakah termasuk tab System Log pada detail user Admin Console (B).
- Spec 069 langkah 80: Membuka Changelog Hardware Stock setelah langkah 79 di Admin Console > Approvals > Hardware Stock: tidak jelas apakah Changelog milik menu Approvals atau menu Hardware Stock; dipertahankan, konfirmasi.
