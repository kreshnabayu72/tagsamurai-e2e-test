# Eliminasi Step: Global Settings > Division

Modul: Division, Sumber: specs/GlobalSettings/Division, Tanggal 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner:** persona aktif dilacak dari Prerequisites dan langkah login, logout, ganti akun, atau ganti company. Langkah yang dijalankan saat persona Distributor atau Partner aktif dikecualikan, termasuk login menuju persona itu. Akun Client (Total Control Client A, B, C, dan seterusnya) bukan Distributor atau Partner, sehingga tidak dikecualikan. Langkah saat persona Principal dipertahankan.
- **B. Halaman detail:** hanya (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya, dan (2) halaman detail client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Global Settings > User, detail user di Fixed Asset > Settings > User, Detail Non-Login User, Detail Role, Detail Brand, dan detail lain tidak termasuk.
- **C. Fitur AI:** tidak ditemukan pada modul ini.
- **D. Menu Approval:** hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- **E. Surface mobile atau Android, serta resize viewport desktop:** langkah yang menguji layout mobile, aplikasi Android, atau bottom sheet mobile. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).
- Langkah login, buka list, dan search yang mendahului halaman detail dipertahankan.

Ringkasan: 5 spek punya eliminasi; 53 dari 2845 langkah bernomor dikecualikan. Langkah yang dikecualikan sebagian (misalnya iterasi persona) dinyatakan di kolom Langkah dikecualikan.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-GS-DIV-E2E-005 | Guided Tooltip Tab Division: Flag Seen, Skip, Overlay, Done, Replay, dan Resize | 36-41 (E) | E | resize viewport desktop (langkah 36, 39); verifikasi setelah resize viewport desktop (langkah 37-38, 40-41) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-DIV-E2E-048 | Setup Column Tabel Division: Reorder, Pin, Reset, dan Search terhadap Kolom Hidden | 15, 19-20, 27-28, 35-36, 42-44 (E) | E | resize viewport desktop (langkah 15, 44); verifikasi setelah resize viewport desktop (langkah 19-20, 27-28, 35-36, 42-43) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-DIV-E2E-062 | Setup Column Modal Changelog: Reorder, Pin/Unpin, dan Reset to Default | 28, 31-32, 36-37, 41-42, 46-47, 51-52, 56-57, 61-62, 65-66, 74-76 (E) | E | resize viewport desktop (langkah 28, 76); verifikasi setelah resize viewport desktop (langkah 31-32, 36-37, 41-42, 46-47, 51-52, 56-57, 61-62, 65-66, 74-75) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-DIV-E2E-079 | Mobile: Screening Halaman, Card List, Row Action, dan Bottom Sheet | 1-31 (E) | E | Menguji surface mobile atau Android | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-DIV-E2E-080 | Mobile: Create dan Edit Division | 1-16 (E) | E | Menguji surface mobile atau Android | Tidak ada ketergantungan yang terdeteksi. |

## Ragu / Perlu Konfirmasi

Tidak ada.
