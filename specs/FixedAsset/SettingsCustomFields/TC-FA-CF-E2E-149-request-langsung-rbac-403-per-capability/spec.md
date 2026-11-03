---
id: TC-FA-CF-E2E-149-request-langsung-rbac-403-per-capability
title: "Request Langsung Ditolak 403 per Capability"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-556
  - TC-FA-CF-558
  - TC-FA-CF-559
  - TC-FA-CF-560
  - TC-FA-CF-561
coverage:
  web: automated
---

# Request Langsung Ditolak 403 per Capability

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor UI: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Tidak ada langkah UI pada spec ini; semua langkah memakai sesi API akun pengirim di bawah.
- Akun pengirim request (token lewat login API tiap akun, kemampuan sesi API aktor disediakan tim BE/FE; tidak ada ganti akun UI), semuanya Company Alpha dengan pola email `<role>_automated_{namaCompany}@qwertysystem.net`:

| Role yang diuji | Pre-setup | Email | Env password |
|---|---|---|---|
| Read Only | #3 | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| Master-Update | #6 | `masterUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MU_PASSWORD` |
| Master-Delete | #7 | `masterDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MD_PASSWORD` |
| No-Capability | #9 | `noCapability_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_NOCAP_PASSWORD` |

  Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11 dan #12): field `Asset Serial Tag`, `Legacy Tag`, dan `Storage Capacity`. Target request ditolak 403 sehingga data tidak berubah. Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE).
- Data Dinamis: Field Name request Create ditolak `Req Update {runId}-149`.
- Kemampuan teknis: klien HTTP; fixture BE untuk membaca field.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah (semua request ditolak). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-556: Create langsung oleh pemegang Update saja

1. Kirim request Create custom field langsung dengan token pemegang Update (Pre-setup #6), payload valid dengan Field Name `Req Update {runId}-149`
2. Verifikasi server merespons 403 Forbidden
3. Verifikasi field `Req Update {runId}-149` tidak dibuat (dibaca lewat fixture BE)

### TC-FA-CF-558: Activate atau Deactivate langsung oleh pemegang Delete saja

4. Kirim request Deactivate langsung untuk field `Asset Serial Tag` dengan token pemegang Delete (Pre-setup #7)
5. Verifikasi request Deactivate direspons 403 Forbidden
6. Kirim request Activate langsung untuk field `Asset Serial Tag` dengan token pemegang Delete (Pre-setup #7)
7. Verifikasi request Activate direspons 403 Forbidden
8. Verifikasi status field `Asset Serial Tag` tidak berubah (dibaca lewat fixture BE)

### TC-FA-CF-559: Delete langsung oleh pemegang Update saja

9. Kirim request Delete langsung untuk field `Legacy Tag` dengan token pemegang Update (Pre-setup #6)
10. Verifikasi server merespons 403 Forbidden
11. Verifikasi field `Legacy Tag` tetap ada (dibaca lewat fixture BE)

### TC-FA-CF-560: request bulk langsung oleh Read Only

12. Kirim request Bulk Delete langsung untuk dua field terpilih (`Asset Serial Tag` dan `Storage Capacity`) dengan token Read Only (Pre-setup #3)
13. Verifikasi request Bulk Delete menerima 403 Forbidden
14. Kirim request Bulk Activate langsung untuk dua field terpilih dengan token Read Only
15. Verifikasi request Bulk Activate menerima 403 Forbidden
16. Kirim request Bulk Deactivate langsung untuk dua field terpilih dengan token Read Only
17. Verifikasi request Bulk Deactivate menerima 403 Forbidden
18. Verifikasi tidak ada field yang berubah atau terhapus (dibaca lewat fixture BE)

### TC-FA-CF-561: baca daftar custom field oleh role tanpa capability

19. Kirim request daftar custom field langsung dengan token No-Capability (Pre-setup #9)
20. Verifikasi server menolak dengan 403 Forbidden
21. Verifikasi respons tidak mengembalikan definisi field

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a dengan Expected respons API (TC-FA-CF-556, 558 sampai 561) tetap di spec FE+BE ini; request hanya mengasersi status respons dan state data (bagian 8b butir 1).
- S-05: TC-FA-CF-557 (Edit langsung oleh pemegang Create saja, dengan klausa "tanpa log") diasersi di spec 132 beserta baseline log; spec ini tidak memuat asersi log.
- Tiap akun role mengirim request lewat sesi API (bukan ganti akun UI); tidak ada konteks UI kedua sehingga `P-2` tidak dipakai.
- Temuan untuk QA:
  - TC-FA-CF-560 menyebut "dua field terpilih" tanpa nama; spec memakai `Asset Serial Tag` dan `Storage Capacity`.
  - TC-FA-CF-556, 558 sampai 561 tidak menyebut payload valid; spec memakai Field Name Dinamis bersuffix dan Data Type `Text`.
  - Email akun role (Pre-setup #3, #6, #7, #9) hanya berpola `<role>_automated_{namaCompany}@qwertysystem.net`.
