# Eliminasi Step: Global Settings > NonLoginUser

Modul: NonLoginUser  
Sumber: specs/GlobalSettings/NonLoginUser  
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
| TC-GS-NLU-E2E-085-list-setup-column-bagian-2 | List Setup Column bagian 2: Pin dan Unpin, Reset to Default, tutup tanpa Save, kolom visible terakhir, cache terpisah dari Login User, dan baris yang tidak muncul | 1, 3-4, 6-8 (E) | E | resize viewport desktop (langkah 1, 8); verifikasi setelah resize viewport desktop (langkah 3-4, 6-7) | Tidak ada ketergantungan yang terdeteksi. |

## Ragu / Perlu Konfirmasi

Tidak ada.
