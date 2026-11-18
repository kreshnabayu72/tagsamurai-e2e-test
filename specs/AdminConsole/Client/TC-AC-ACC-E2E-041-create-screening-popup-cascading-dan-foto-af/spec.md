---
id: TC-AC-ACC-E2E-041-create-screening-popup-cascading-dan-foto-af
title: "Popup New Client: Screening, Cascading Country-State-City, dan Preview Photo (Active-Full)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-65
  - TC-AC-ACC-121
  - TC-AC-ACC-122
coverage:
  web: automated
---

# Popup New Client: Screening, Cascading Country-State-City, dan Preview Photo (Active-Full)

## Prerequisites

- Mode: FE+BE. Tidak ada data yang dibuat.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Berkas uji `logo.jpg` (JPG 500 KB) tersedia di mesin uji; kemampuan memilih berkas pada ImagePicker Photo dan mengamati request jaringan (untuk memastikan klik `[✕]` pada thumbnail tidak mengirim request).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-65: Screening popup New Client

1. Klik `[+ New Client]`
2. Verifikasi header popup: Title "New Client" dan tombol silang `[✕]`
3. Verifikasi Section "Company Information": Photo (ImagePicker PNG/JPG/JPEG, maks 1 MB)
4. Verifikasi Company Name* dengan placeholder "Enter company name"
5. Verifikasi Client Code dengan placeholder "Auto-generated or enter manually" dan helper "Letters, numbers, hyphens, underscores, and dots only"
6. Verifikasi Company Email dengan placeholder "Enter company email"
7. Verifikasi Industry (dropdown searchable) dengan placeholder "Select industry"
8. Verifikasi Website dengan placeholder "Enter website URL"
9. Verifikasi Fax dengan placeholder "Enter fax number"
10. Verifikasi Section "PIC": PIC Name* dengan placeholder "Enter PIC name"
11. Verifikasi PIC Email* dengan placeholder "Enter PIC email"
12. Verifikasi PIC Phone dengan placeholder "Enter PIC phone"
13. Verifikasi Section "Address": Address* (textarea 3 baris) dengan placeholder "Enter address"
14. Verifikasi Country* dengan placeholder "Select country"
15. Verifikasi State* dengan placeholder "Select state" dan disabled
16. Verifikasi City* dengan placeholder "Select city" dan disabled
17. Verifikasi Postal Code* dengan placeholder "Enter postal code"
18. Verifikasi Section "Partner & Group": Partner (multi-select) dengan placeholder "Select partner(s) (optional)" dan helper "You can also link clients through subscription allocation."
19. Verifikasi Select Group* (tree) dengan placeholder "Select group"
20. Verifikasi Section "Default User" ditampilkan dalam highlight box: First Name* dengan placeholder "Enter first name"
21. Verifikasi Last Name* dengan placeholder "Enter last name"
22. Verifikasi Email* dengan placeholder "Enter email"
23. Verifikasi Position dengan placeholder "Enter position (optional)"
24. Verifikasi Division* dengan placeholder "Enter division"
25. Verifikasi helper "These will be created as the first position (if filled) and division for this client's Global Settings."
26. Verifikasi info box (severity info) "Activation email will be sent when the first subscription is activated, not immediately after account creation."
27. Verifikasi warning (severity warning) "This email will become the permanent Default User and cannot be deactivated. Use a role-based email (e.g. admin@company.com)."
28. Verifikasi footer Row 1: checkbox "Stay on this form after submitting" dalam keadaan unchecked
29. Verifikasi footer Row 2: `[Clear Field]` (text, primary) dan `[Submit]` (Success), rata kanan
30. Verifikasi lebar popup 600px dan body dapat di-scroll
31. Buka dropdown Industry
32. Verifikasi dropdown Industry memuat 15 opsi: Retail, Manufacturing, Logistics & Warehousing, Healthcare, Education, Finance & Banking, Technology, Construction, Hospitality, Government, Transportation, Telecommunications, Oil & Gas, Agriculture, Others
33. Ketik "Health" pada pencarian dropdown Industry
34. Verifikasi hanya opsi "Healthcare" yang tersisa
35. Pilih opsi "Healthcare" (menutup dropdown)

### TC-121: Country, State, City cascading

36. Verifikasi State dan City disabled pada keadaan awal
37. Pilih Country "Indonesia"
38. Verifikasi State enabled
39. Verifikasi City tetap disabled
40. Pilih State "DKI Jakarta"
41. Verifikasi City enabled
42. Pilih City "Jakarta Selatan"
43. Ubah Country menjadi "Malaysia"
44. Verifikasi State kembali ke placeholder "Select state" (ter-reset)
45. Verifikasi City kembali ke placeholder "Select city" (ter-reset)

### TC-122: Preview Photo

46. Pilih berkas `logo.jpg` (JPG 500 KB) pada ImagePicker Photo
47. Verifikasi file picker memfilter format PNG/JPG/JPEG
48. Verifikasi preview thumbnail Photo tampil
49. Klik ikon `[✕]` pada thumbnail Photo
50. Verifikasi pilihan Photo kosong kembali (placeholder upload)
51. Verifikasi klik `[✕]` pada thumbnail tidak mengirim request API (aksi lokal)

### Penutup

52. Klik `[✕]` di header popup
53. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
54. Klik `[Leave]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): "Pilih opsi Healthcare" menutup dropdown Industry sebelum TC-121; "Ubah Country menjadi Malaysia" memakai negara lain (TC-121 langkah 5 tidak menyebut nilai; Malaysia dipakai sesuai TC-523); penutup `[✕]`, dialog `Unsaved Changes`, `[Leave]` menutup form dirty (S-08).
- Alasan di atas 35 langkah (sekitar 55 langkah): satu popup, satu role, tanpa aksi tulis; tiap placeholder dan helper TC-65 adalah klausa terpisah (S-01); tiap bagian berdiri sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - TC-121 langkah 5 ("Ubah Country ke negara lain") tidak menyebut negara; spec memakai Malaysia.
