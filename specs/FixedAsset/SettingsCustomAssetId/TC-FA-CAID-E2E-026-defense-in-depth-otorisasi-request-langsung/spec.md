---
id: TC-FA-CAID-E2E-026-defense-in-depth-otorisasi-request-langsung
title: "Defense-in-Depth: Request Save dan Toggle Langsung Tanpa Capability dan pada Plan Starter"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-303
  - TC-FA-CAID-304
  - TC-FA-CAID-305
coverage:
  web: automated
---

# Defense-in-Depth: Request Save dan Toggle Langsung Tanpa Capability dan pada Plan Starter

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite. Akun Total Control dipakai untuk membaca state sesudah request (langkah 3 sampai 7 dan 10 sampai 14).
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 (Pre-setup No 11) ke kondisi awal di `beforeEach` dan `after` lewat sesi API aktor (klien HTTP dan token sesi API disediakan tim FE; token tidak dihitung sebagai sesi web).
- Role yang diuji untuk TC-FA-CAID-303 dan TC-FA-CAID-304 (Company Alpha; email `<prefix>_automated_{namaCompany}@qwertysystem.net`, password dari env, tidak ditulis di spec atau fixture). Langkah tiap role identik, hanya token sesi API yang berbeda:

| Role | Pre-setup | Prefix email | Env password |
|---|---|---|---|
| Read Only | No 2 | `readOnly` | `Spectra.env.FA_RO_PASSWORD` |
| Config-Read (Manage asset ID configuration hanya Read) | No 4 | `configRead` | `Spectra.env.FA_CFGREAD_PASSWORD` |
| Master-Data-Only (Manage asset master data tanpa Manage asset ID configuration) | No 5 | `masterDataOnly` | `Spectra.env.FA_MDONLY_PASSWORD` |
| Tanpa Role Terkait | No 7 | `noRelatedRole` | `Spectra.env.FA_NOROLE_PASSWORD` |

- Akun TC-FA-CAID-305: Config-Update (Manage asset ID configuration dengan Read dan Update, Pre-setup No 3) pada Company Starter (Pre-setup No 13). Email akun pada Company Starter disediakan tim FE/BE (Pre-setup No 13 TC). Password dari `Spectra.env.FA_STARTER_CFGUPD_PASSWORD` (kolom Akun dan Env Var Pre-setup No 13).
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company). Data Pre-setup No 11: A1 Active `JKT/LAP/T490/0926/1`, A2 Draft `JKT/LAP/T490/0926/2`, A3 Waiting for Approval `JKT/LAP/T490/0000/3`, A4 Disposed `JKT/LAP/T490/0926/4`, A5 Deleted. Data Pre-setup No 13: Company Starter dengan konfigurasi tersimpan B1 dan aset S1 `JKT/LAP/T490/0926/1`. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): klien API dan penyunting request pada sesi otomasi (Pre-setup No 26) untuk mengirim request Save dan Toggle langsung ke server dengan token sesi API aktor; Company Starter dan seed konfigurasinya.
- State: tidak ada perubahan tersimpan yang diharapkan; semua request ditolak. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-303: Request Save langsung tanpa capability Update ditolak HTTP 403

Untuk setiap baris tabel Role yang diuji (langkah 1 sampai 2):

1. Kirim request Save konfigurasi langsung ke server dengan token sesi API role pada baris tabel, Separator `- (Dash)`, formula valid delapan segmen
2. Verifikasi server mengembalikan HTTP 403 Forbidden

Setelah keempat role:

3. Buka Fixed Asset > Assets > All Assets
4. Verifikasi Asset ID A1 sampai A4 tidak berubah
5. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
6. Verifikasi konfigurasi tersimpan tidak berubah: Separator tetap `/ (Slash)`
7. Verifikasi konfigurasi tersimpan tidak berubah: Master Switch tetap ON

### TC-FA-CAID-304: Request Toggle langsung tanpa capability Update ditolak HTTP 403

Untuk setiap baris tabel Role yang diuji (langkah 8 sampai 9):

8. Kirim request Toggle langsung ke server dengan token sesi API role pada baris tabel, status Master Switch `Inactive`
9. Verifikasi server mengembalikan HTTP 403 Forbidden

Setelah keempat role:

10. Buka Fixed Asset > Assets > All Assets
11. Verifikasi Asset ID A1 sampai A4 tidak berubah
12. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
13. Verifikasi konfigurasi tersimpan tidak berubah: Separator tetap `/ (Slash)`
14. Verifikasi konfigurasi tersimpan tidak berubah: Master Switch tetap ON

### TC-FA-CAID-305: Request Save dan Toggle langsung pada plan Starter ditolak server

15. Ganti akun: logout akun Total Control, lalu login sebagai Config-Update pada Company Starter (Pre-setup No 13)
16. Kirim request Save langsung ke server dengan Separator `- (Dash)`
17. Verifikasi request Save ditolak server
18. Kirim request Toggle langsung ke server dengan status `Inactive`
19. Verifikasi request Toggle ditolak server
20. Buka Fixed Asset > Assets > All Assets
21. Verifikasi Asset ID S1 tetap `JKT/LAP/T490/0926/1`
22. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
23. Verifikasi konfigurasi tersimpan tetap Separator `/ (Slash)`
24. Verifikasi konfigurasi tersimpan tetap Master Switch ON

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- `K-1`: spec defense-in-depth dengan Expected respons API (status HTTP dan state data lewat UI) tetap FE+BE walau tumpang tindih dengan `tc-settings-custom-asset-id-backend.md`; TC granular tetap sumber dan BE mencatatnya pada tingkat endpoint.
- Langkah 1, 8, 16, dan 18 mengirim request langsung lewat klien HTTP tanpa browser; asersinya hanya status respons dan state data yang dibaca lewat UI (bagian 8b butir 1). Perilaku FE untuk respons yang sama tidak diasersi.
- Langkah penghubung (tanpa `Verifikasi`): langkah 3, 5, 10, 12, 20, dan 22 (membuka layar pembaca state), serta langkah 15 (ganti akun; hook `after` mengembalikan sesi ke akun default suite).
- Pola berulang: langkah 1 sampai 2 diulang untuk 4 role pada tabel, langkah 8 sampai 9 diulang untuk 4 role pada tabel.
- Pembagian TC lintas spec: TC-FA-CAID-303, 304, dan 305 juga ada di spec 098 (asersi absence entri log atas request yang sama, S-05); spec ini hanya mengasersi status respons dan state data.
- S-01, klausa digabung dengan alasan: "Asset ID A1 sampai A4 tidak berubah" (langkah 4 dan 11) satu `Verifikasi` karena Expected TC-FA-CAID-303 b dan 304 b menyebutnya satu klausa seragam atas aset seed yang sama; Separator dan Master Switch dipecah per klausa.
- Temuan untuk QA:
  - Expected TC-FA-CAID-303 b, TC-FA-CAID-304 b, dan TC-FA-CAID-305 c memuat "tidak memuat entri baru" pada Modal Changelog, System Log, dan Activity Log. Asersi absence log atas request langsung yang ditolak tidak ditulis di spec kelas a ini (S-05, bagian 8b butir 1); asersi itu ada di spec absence 098 yang memuat TC-FA-CAID-303, 304, dan 305 dengan request ini sebagai pemicu dan baseline sendiri.
  - Expected TC-FA-CAID-305 a menyebut alasan penolakan ("plan tidak memiliki toggle Asset ID Config dan tidak ada mass update yang berjalan"); alasan dan ketiadaan mass update tidak punya langkah observasi di TC, sehingga spec hanya mengasersi penolakan dan state data (Asset ID S1 dan konfigurasi).
