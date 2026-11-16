# Eliminasi Step: Global Settings > CustomFieldUser

Modul: CustomFieldUser, Sumber: specs/GlobalSettings/CustomFieldUser, Tanggal 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner:** persona aktif dilacak dari Prerequisites dan langkah login, logout, ganti akun, atau ganti company. Langkah yang dijalankan saat persona Distributor atau Partner aktif dikecualikan, termasuk login menuju persona itu. Akun Client (Total Control Client A, B, C, dan seterusnya) bukan Distributor atau Partner, sehingga tidak dikecualikan. Langkah saat persona Principal dipertahankan.
- **B. Halaman detail:** hanya (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya, dan (2) halaman detail client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Global Settings > User, detail user di Fixed Asset > Settings > User, Detail Non-Login User, Detail Role, Detail Brand, dan detail lain tidak termasuk.
- **C. Fitur AI:** tidak ditemukan pada modul ini.
- **D. Menu Approval:** hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- **E. Surface mobile atau Android, serta resize viewport desktop:** langkah yang menguji layout mobile, aplikasi Android, atau bottom sheet mobile. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).
- Langkah login, buka list, dan search yang mendahului halaman detail dipertahankan.

Ringkasan: 5 spek punya eliminasi; 53 dari 6232 langkah bernomor dikecualikan. Langkah yang dikecualikan sebagian (misalnya iterasi persona) dinyatakan di kolom Langkah dikecualikan.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-GS-UCF-E2E-005 | Guided Tooltip Tab Custom Field: Konten 3 Step, Navigasi Keyboard, Fokus Tooltip Box, Aktor Read Only, dan Resize atau Navigasi Keluar | 56-59, 64 (E) | E | resize viewport desktop (langkah 56, 64); verifikasi setelah resize viewport desktop (langkah 57-59) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-UCF-E2E-046 | Mobile Android: Selection Mode Long-press, Keluar dari Mode Multi-select, Select All, dan Bulk Delete Custom Field | 1-41 (E) | E | Menguji surface mobile atau Android | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-UCF-E2E-052 | Filter Panel Tabel Utama Custom Field: Screening, Logika OR dan AND, Chip, Opsi Dinamis, Draft, Clear Field, dan Retensi F5 | 70, 73-75, 77 (E) | E | resize viewport desktop (langkah 70, 77); verifikasi setelah resize viewport desktop (langkah 73-75) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-UCF-E2E-056 | Overlay Column Visibility dan Modal Setup Column Tabel Custom Field: Screening, Hide, Reorder, Pin, Reset, Penutupan, dan Independensi dari Modal Changelog | 59, 66-67, 69, 74-75, 77-78, 80, 82-83, 85-86, 88, 90-96 (E) | E | resize viewport desktop (langkah 59, 90, 96); verifikasi setelah resize viewport desktop (langkah 66-67, 69, 74-75, 77-78, 80, 82-83, 85-86, 88, 91-95) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-UCF-E2E-073 | Sinkronisasi Custom Field ke Kolom Curated Fixed Asset Settings User, Admin Console Settings User, dan Popup Total User Detail Admin Console Settings Group | 37-41 (B) | B | Membuka, memverifikasi, atau beroperasi di halaman detail user Admin Console > Settings > User (Detail Rahmat Hidayat, accordion Custom Field, kembali ke list) | Tidak ada ketergantungan yang terdeteksi. |

## Ragu / Perlu Konfirmasi

- Spec 073 langkah 41 (Kembali ke Admin Console > Settings > User dari Detail Rahmat Hidayat): diperlakukan B bersama langkah 37-40 karena aksi keluar dari halaman detail. Konfirmasi.
