---
id: TC-FA-PREF-E2E-155-status-tombol-save-changes-dan-cancel-pada-form-pristine-dan-berubah
title: "Status Tombol [Save changes] dan [Cancel]: Disabled pada Form Pristine, Enabled saat Berubah, Kembali Disabled saat Dikembalikan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-18
  - TC-FA-PREF-19
  - TC-FA-PREF-20
coverage:
  web: automated
---

# Status Tombol [Save changes] dan [Cancel]: Disabled pada Form Pristine, Enabled saat Berubah, Kembali Disabled saat Dikembalikan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi; In-service Date Source tersimpan "Activation date". Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API). Spec tidak menyimpan perubahan; semua ubahan form dikembalikan ke nilai tersimpan sebelum spec berakhir.
- Kemampuan teknis: pengamatan request jaringan dari browser (hanya mengamati, tanpa mengubah respons), disediakan tim FE, untuk klausa "tidak menghasilkan request" pada TC-FA-PREF-18.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-18: Disabled tanpa tooltip saat form pristine

1. Verifikasi `[Save changes]` dan `[Cancel]` tetap tampil dan Disabled
2. Hover `[Save changes]`
3. Verifikasi tidak ada tooltip pada `[Save changes]`
4. Hover `[Cancel]`
5. Verifikasi tidak ada tooltip pada `[Cancel]`
6. Klik `[Save changes]`
7. Klik `[Cancel]`
8. Verifikasi klik pada keduanya tidak menghasilkan dialog, toast, maupun request

### TC-FA-PREF-19: Enabled saat form berbeda dari nilai tersimpan

9. Ubah In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
10. Verifikasi `[Save changes]` Enabled
11. Verifikasi `[Cancel]` Enabled
12. Ubah In-service Date Source kembali menjadi "Activation date"

### TC-FA-PREF-20: Kembali Disabled saat nilai dikembalikan

13. Ubah In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
14. Ubah In-service Date Source kembali menjadi "Activation date"
15. Verifikasi `[Save changes]` dan `[Cancel]` Disabled
16. Hover `[Save changes]`
17. Verifikasi tidak ada tooltip pada `[Save changes]`
18. Hover `[Cancel]`
19. Verifikasi tidak ada tooltip pada `[Cancel]`

## Notes

- Langkah penghubung (S-03, S-09): langkah 12 (mengembalikan In-service Date Source ke nilai tersimpan agar TC-FA-PREF-20 dimulai dari form pristine dan agar form tidak dirty di akhir TC-FA-PREF-19). Layar Preferences dibuka hook `beforeEach` suite, sehingga langkah TC "Buka Tab Preferences" tidak diulang.
- Langkah 2 sampai 5 dan 16 sampai 19 (hover lalu asersi tooltip): TC-FA-PREF-18 menyebut hover pada langkah TC; TC-FA-PREF-20 menyebut "tanpa tooltip" pada Expected tanpa langkah hover, sehingga langkah 16 dan 18 ditambahkan agar klausa tooltip dapat diasersi (S-14).
- Urutan TC dalam spec: TC-FA-PREF-18, 19, 20.
- Temuan untuk QA: TC-FA-PREF-20 tidak memuat langkah hover untuk klausa "tanpa tooltip"; spec menambahkan langkah hover sebagai langkah penghubung.
