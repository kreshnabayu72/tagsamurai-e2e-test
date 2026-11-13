# Usulan Naik ke "Di Dalam Filter": Admin Console > License Allocation (Subscription)

Modul: Admin Console > License Allocation > Subscription (Add, Edit, Activate Trial, Cancel, Convert, Renew, Auto-Archive, Log, Konfigurasi Platform)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/LicenseAllocationSubscription`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-036 | Add: Group Manager Ancestor dan Start Date 29 Februari | High | Group Manager ancestor menyangkut akses, dan tanggal kabisat bisa salah masa berlaku | Belum ada skrip | tidak |
| E2E-044 | Form: State Submitting dan Klik Ganda Add dan Activate Trial | High | Klik ganda bisa membuat trial ganda | Belum ada skrip | tidak |
| E2E-050 | Activate Trial: Kuota Kosong dan Batas Bawah | High | Trial bisa aktif tanpa kuota atau melewati batas | Belum ada skrip | tidak |
| E2E-137 | Multi-konteks: Dua Admin Sesi Bersamaan Principal | High | Konkurensi dua admin pada principal yang sama | Belum ada skrip | tidak |
| E2E-142 | Klik Ganda Cancel Subscription dan Convert | High | Cancel dan convert ganda merusak status subscription | Belum ada skrip | tidak |
| E2E-143 | Klik Ganda Cancel Request dan Save Edit, State Submitting Save | High | Klik ganda bisa memproses dua kali | Belum ada skrip | tidak |
| E2E-160 | Konfigurasi Platform Live: Push Update Plan, Ceiling Trial, dan Approval Timeout | High | Perubahan plan live berdampak ke semua client | Belum ada skrip | tidak |
| E2E-162 | Multi-konteks: Race Add, Cancel dan Renew, serta Convert Ganda | High | Konkurensi pada siklus hidup subscription | Belum ada skrip | tidak |
| E2E-055 | State Tenant: Cancel, Job, dan Suspend Trial pada Client Suspended atau Expired | Medium | Write lockdown: aksi tulis pada tenant Suspended atau Expired harus ditolak | Belum ada skrip | tidak |
| E2E-150 | State Tenant: Trial Expired pada Dropdown, Convert, dan Activate Trial | Medium | Tenant expired tidak boleh mengonversi atau mengaktifkan trial | Belum ada skrip | tidak |
| E2E-156 | Subscription Log: Urutan, Immutability, dan Edit No-Op | Medium | Jejak audit subscription harus tepat | Belum ada skrip | tidak |
| E2E-161 | Modul Konsumen: Auto-Archive Client setelah Cancel Subscription Terakhir | Medium | Client bisa ter-archive secara salah | Belum ada skrip | tidak |
| E2E-144 | Kondisi Sisa: Ceiling, Back Browser, Plan Archive, Tier, Toast | Medium | Kondisi sisa ceiling dan tier bisa membiarkan plan yang salah tersimpan | Gagal: seed trial ditolak 422 (trialDurationDays dan trialConcurrentUserQuota kosong) | ya (be-bug BT-AC-CS-6, ems#56; seed trial 422) |

## Yang Tidak Dinaikkan

- E2E-031: validasi Duration. Validasi format.
- E2E-007, E2E-015, E2E-045, E2E-091, E2E-095, E2E-098, E2E-109, E2E-110, E2E-145: format ID, anchor nama, guided tooltip, filter, setup column, dan changelog setup column. Tampilan.
- E2E-147: edit duration tanggal 29 Februari, dampak rendah (Low).
- E2E-163: retry setelah timeout dan toast error. Dampak resilience sedang.

## Catatan untuk FE/QA

- E2E-144 gagal di seed trial (422) karena field wajib trial kosong. Ini masalah seed, bukan bug UI. Perlu dicek BE (BT-AC-CS-6).
- E2E-160 di modul ini (Konfigurasi Platform Live) berbeda dari E2E-160 di Plans Licensing Lifecycle Settings. Keduanya dinaikkan dan ditulis per modul.
