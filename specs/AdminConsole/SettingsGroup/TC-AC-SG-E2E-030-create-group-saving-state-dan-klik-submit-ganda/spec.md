---
id: TC-AC-SG-E2E-030-create-group-saving-state-dan-klik-submit-ganda
title: "Create Group: Saving State dan Klik Submit Ganda"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-104
  - TC-AC-SG-106
coverage:
  web: automated
---

# Create Group: Saving State dan Klik Submit Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama dari TC diberi suffix per run, S-12):

| TC | Nama di TC | Nama di spec |
|---|---|---|
| TC-AC-SG-104 | `Region Saving` (level 1) | `Region Saving-{runId}-030` |
| TC-AC-SG-106 | `Region Ganda` (level 1) | `Region Ganda-{runId}-030` |

- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk menahan respons request Create Group dan melepasnya (Pre-setup #38) serta menghitung request Create Group yang terkirim; Fixture BE (penghapusan data milik spec) disediakan tim FE/BE (lihat `suite.md`). Penahanan respons hanya untuk mengamati state UI dan bukan kegagalan yang dipaksa.
- Jumlah group dasar (N) dibaca dari label root "All Groups (N)"; tidak memakai angka absolut.
- Pemulihan: intercept dilepas pada langkah 7 dan di hook `after`; hook `after` menghapus group milik spec lewat Fixture BE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-104: Saving state tombol Submit

1. Aktifkan penahanan respons pada request Create Group (intercept)
2. Klik `[+] Group` di Sidebar Group Tree
3. Ketik `Region Saving-{runId}-030` pada Group Name, klik `[Submit]`
4. Verifikasi tombol `[Submit]` menampilkan indikator loading
5. Verifikasi tombol `[Submit]` disabled
6. Verifikasi field Group Name, `[Clear Field]`, dan `[✕]` ikut disabled hingga respons diterima
7. Lepas tahanan respons pada request Create Group
8. Verifikasi popup menutup
9. Verifikasi toast sukses: "Success, group has been created."

### TC-AC-SG-106: Klik Submit ganda

10. Tunggu toast lama hilang otomatis
11. Catat jumlah group N pada label root "All Groups (N)" di Sidebar Group Tree
12. Klik `[+] Group` di Sidebar Group Tree
13. Ketik `Region Ganda-{runId}-030` pada Group Name
14. Klik `[Submit]` dua kali berturut-turut secepat mungkin
15. Verifikasi hanya satu group `Region Ganda-{runId}-030` yang dibuat (label root "All Groups (N+1)" dan satu node `Region Ganda-{runId}-030` di sidebar)
16. Verifikasi permintaan kedua tidak dikirim (hanya satu request Create Group terkirim)
17. Verifikasi toast sukses tampil sekali: "Success, group has been created."

## Notes

- Langkah penghubung (S-03): langkah 10 (menunggu toast TC-AC-SG-104 hilang agar hitungan toast TC-AC-SG-106 tidak tertukar, R-12) dan langkah 11 (baseline jumlah group).
- Langkah 1 dan 7 adalah pemicu tahan respons; sesuai bagian 8b butir 11, tidak ada asersi absence toast sebelum respons dilepas.
- Temuan untuk QA:
  - TC-AC-SG-104 Expected butir b "toast sukses tampil" tidak menyebut teksnya; spec memakai teks toast Create pada TC-AC-SG-106.
  - TC-AC-SG-106 Expected "permintaan kedua tidak dikirim karena tombol disabled" tidak punya cara observasi di TC; spec mengasersinya lewat hitungan request pada intercept (kemampuan disediakan tim FE).
