# Eliminasi Step: Global Settings > GeneralSettings

Modul: GeneralSettings, Sumber: specs/GlobalSettings/GeneralSettings, Tanggal 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner:** persona aktif dilacak dari Prerequisites dan langkah login, logout, ganti akun, atau ganti company. Langkah yang dijalankan saat persona Distributor atau Partner aktif dikecualikan, termasuk login menuju persona itu. Akun Client (Total Control Client A, B, C, dan seterusnya) bukan Distributor atau Partner, sehingga tidak dikecualikan. Langkah saat persona Principal dipertahankan.
- **B. Halaman detail:** hanya (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya, dan (2) halaman detail client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Global Settings > User, detail user di Fixed Asset > Settings > User, Detail Non-Login User, Detail Role, Detail Brand, dan detail lain tidak termasuk.
- **C. Fitur AI:** tidak ditemukan pada modul ini.
- **D. Menu Approval:** hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- **E. Surface mobile atau Android, serta resize viewport desktop:** langkah yang menguji layout mobile, aplikasi Android, atau bottom sheet mobile. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).
- Langkah login, buka list, dan search yang mendahului halaman detail dipertahankan.

Ringkasan: 5 spek punya eliminasi; 58 dari 1450 langkah bernomor dikecualikan. Langkah yang dikecualikan sebagian (misalnya iterasi persona) dinyatakan di kolom Langkah dikecualikan.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-GS-GSET-E2E-010 | Trigger, flag, penutupan | 30-36 (E) | E | resize viewport desktop (langkah 30, 36); verifikasi setelah resize viewport desktop (langkah 31-35) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-GSET-E2E-012 | Mobile screening, bottom sheet, tooltip ketuk, Read Only | 1-31 (E) | E | Menguji surface mobile atau Android | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-GSET-E2E-013 | Mobile dialog | 1-22 (E) | E | Menguji surface mobile atau Android | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-GSET-E2E-035 | Changelog General Settings: Setup Column Pin/Unpin, Hide/Unhide, Reorder, dan Reset to Default dengan Save | 7, 10-11, 13-15 (E) | E | resize viewport desktop (langkah 15); verifikasi setelah resize viewport desktop (langkah 7, 10-11, 13-14) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-GSET-E2E-047 | Timestamp lintas produk | 1-2 (A) | A | Langkah dijalankan saat persona staf Distributor PT Maju Bersama aktif (akun pertama di hook before) | Langkah 4-5 (persona Client PT Sentosa Abadi) dipertahankan dan tidak bergantung pada langkah 1-2; nilai {tUTC1} hanya diverifikasi di langkah 2 (dikecualikan). |

## Ragu / Perlu Konfirmasi

- Spec 047 langkah 3: logout dari persona Distributor (PT Maju Bersama) lalu login sebagai Client (PT Sentosa Abadi). Langkah dipertahankan karena tujuan login bukan Distributor atau Partner. Konfirmasi.
- Spec 035 langkah 6: Langkah campuran: memuat resize viewport bersama aksi lain dalam satu langkah; dipertahankan, konfirmasi.
