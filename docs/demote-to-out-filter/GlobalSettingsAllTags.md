# Eliminasi Step: Global Settings > AllTags

Modul: AllTags, Sumber: specs/GlobalSettings/AllTags, Tanggal 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner:** persona aktif dilacak dari Prerequisites dan langkah login, logout, ganti akun, atau ganti company. Langkah yang dijalankan saat persona Distributor atau Partner aktif dikecualikan, termasuk login menuju persona itu. Akun Client (Total Control Client A, B, C, dan seterusnya) bukan Distributor atau Partner, sehingga tidak dikecualikan. Langkah saat persona Principal dipertahankan.
- **B. Halaman detail:** hanya (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya, dan (2) halaman detail client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Global Settings > User, detail user di Fixed Asset > Settings > User, Detail Non-Login User, Detail Role, Detail Brand, dan detail lain tidak termasuk.
- **C. Fitur AI:** tidak ditemukan pada modul ini.
- **D. Menu Approval:** hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Langkah yang dikecualikan sebagai D di modul ini: TC-GS-TAG-E2E-051 langkah 1, 24-28; TC-GS-TAG-E2E-055 langkah 34-36; TC-GS-TAG-E2E-063 langkah 25-26, 37-38; TC-GS-TAG-E2E-064 langkah 1-2, 4-8, 12-14. Approve atau Reject lewat sesi API di luar menu Admin Console > Approvals tidak dikecualikan.
- **E. Surface mobile atau Android, serta resize viewport desktop:** langkah yang menguji layout mobile, aplikasi Android, atau bottom sheet mobile. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).
- Langkah login, buka list, dan search yang mendahului halaman detail dipertahankan.

Ringkasan: 7 spek punya eliminasi; 59 dari 4008 langkah bernomor dikecualikan. Langkah yang dikecualikan sebagian (misalnya iterasi persona) dinyatakan di kolom Langkah dikecualikan.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-GS-TAG-E2E-015 | Mobile: Tanpa Bulk Delete/Resolve/Remove, Activate GPS Hanya Entri Manual, dan Visibilitas Tombol per Tab dan Role | 1-32 (E) | E | Menguji surface mobile atau Android | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-TAG-E2E-040 | Audit TAG: Overlay Select TAG Type, Screening Popup Audit, Daftar Eligible, Combined, Empty State S-06, dan Tombol per Tab | 28-30 (E) | E | resize viewport desktop (langkah 28, 30); verifikasi setelah resize viewport desktop (langkah 29) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-TAG-E2E-051 | Delete: Efek Lintas Modul (Waiting for Approval di Approvals, Unit Stok Official, Unit Self-Purchased) | 1, 24-28 (D) | D | Masuk atau beroperasi di Admin Console > Approvals (menu Approval belum dibuat) | Tidak ada langkah yang dipertahankan bergantung pada langkah 24-28. |
| TC-GS-TAG-E2E-055 | Delete by Scan: Penolakan Paired/Reserved T-34, Waiting for Approval T-36, Combined, Tak Dikenal T-08/T-09, dan Sesi Tanpa Log | 34-36 (D) | D | Masuk atau beroperasi di Admin Console > Approvals (menu Approval belum dibuat) | Tidak ada langkah yang dipertahankan bergantung pada langkah 34-36; langkah 37-40 kembali ke persona Client dan tetap dipertahankan. |
| TC-GS-TAG-E2E-063 | Sinkronisasi Admin Console: Pemakaian Stok, Kolisi sebagai Activation Collision, Approve, Reject, dan Perubahan Alokasi Kuota | 25-26, 37-38 (D) | D | Masuk atau beroperasi di Admin Console > Approvals (menu Approval belum dibuat) | Langkah 29-33 (status Available, kartu GPS, TAG Log) memverifikasi hasil persetujuan langkah 28 (via sesi API Principal, dipertahankan) sehingga tetap bermakna. Langkah 41-46 memverifikasi hasil penolakan langkah 38 yang dikecualikan; tanpa aksi itu verifikasi yang tersisa tidak memiliki hasil yang dituju; perlu ditinjau. |
| TC-GS-TAG-E2E-064 | Approve/Reject Kolisi Ditolak saat Tag Sudah Dihapus tetapi Event Delete Belum Diproses | 1-2, 4-8, 12-14 (D) | D | Masuk atau beroperasi di Admin Console > Approvals (menu Approval belum dibuat) | Langkah 3 (hapus DD-03 lewat API, dipertahankan) menjadi prasyarat langkah 4-8 yang dikecualikan. Langkah 9-11 dipertahankan dan memverifikasi hasil pemrosesan event yang bergantung pada langkah 2 dan 4 (dikecualikan); perlu ditinjau. |
| TC-GS-TAG-E2E-077 | Setup Column Registri: Pin Hideable dan Curated, Batas Pin Ketiga, dan Reset to Default | 1, 5-6, 8-9, 13-15, 22-23, 25-28 (E) | E | resize viewport desktop (langkah 1, 28); verifikasi setelah resize viewport desktop (langkah 5-6, 8-9, 13-15, 22-23, 25-27) | Tidak ada ketergantungan yang terdeteksi. |

## Ragu / Perlu Konfirmasi

- Spec 015 (E): seluruh langkah 1-32 berada di aplikasi mobile/Android (registri mobile, Activate lewat aplikasi, login Read Only di aplikasi Android). Dikecualikan seluruhnya.
- Spec 064 langkah 9 (verifikasi tidak ada TAG Code yang diterbitkan): surface verifikasi tidak disebut; tidak dikecualikan. Konfirmasi.
- Spec 092 langkah 15, 17: Langkah campuran: memuat resize viewport bersama aksi lain dalam satu langkah; dipertahankan, konfirmasi.
